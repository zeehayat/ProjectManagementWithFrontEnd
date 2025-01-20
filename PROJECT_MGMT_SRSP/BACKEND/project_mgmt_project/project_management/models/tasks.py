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

        if is_new or (old_instance and old_instance.assigned_to != self.assigned_to):
            # Notify assigned user if the task is new or reassigned
            if self.assigned_to:
                Notification.objects.create(
                    user=self.assigned_to,
                    message=f"You have been assigned a new task: {self.name}."
                )

        # Notify the task assigner if notes or attachments were updated
        if old_instance:
            if old_instance.assignee_notes != self.assignee_notes:
                Notification.objects.create(
                    user=self.project.owners.first().user,
                    message=f"The assignee updated notes for the task: {self.name}."
                )
