from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

from project_management.models.attachment import Attachment
from project_management.models.notification import Notification


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tasks")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    assignee_notes = models.TextField(blank=True, null=True)
    assigned_person_notes = models.TextField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)

    attachments = models.ManyToManyField(Attachment, blank=True, related_name="tasks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_late(self):
        return self.due_date and self.status != "Completed" and self.due_date < timezone.now().date()
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_instance = Task.objects.get(pk=self.pk) if not is_new else None

        super().save(*args, **kwargs)  # Save the instance

        # Notify the assigned user if the task is new or reassigned
        if is_new or (old_instance and old_instance.assigned_to != self.assigned_to):
            if self.assigned_to:
                Notification.objects.create(
                    user=self.assigned_to,
                    message=f"You have been assigned a new task: {self.name}.",
                )

        # Notify the assigner about task updates
        if old_instance:
            changes = []
            if old_instance.assignee_notes != self.assignee_notes:
                changes.append("notes updated")
            if old_instance.status != self.status:
                changes.append(f"status changed to {self.status}")
            if old_instance.attachments.count() != self.attachments.count():
                changes.append("attachments updated")

            if changes and self.project.owners.exists():
                assigner = self.project.owners.first().user
                Notification.objects.create(
                    user=assigner,
                    message=f"The task '{self.name}' was updated by {self.assigned_to.username}: {', '.join(changes)}.",
                )
