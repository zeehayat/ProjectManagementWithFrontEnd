from django.db import models
from django.contrib.auth.models import User

from project_management.models.notification import Notification
from project_management.models.task_history import TaskHistory
from project_management.models.tasks import Task


class TaskExtensionRequest(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="extension_requests")
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_days = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=20,
                              choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")],
                              default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        old_status = None if is_new else TaskExtensionRequest.objects.get(pk=self.pk).status

        super().save(*args, **kwargs)  # Save the request

        # Log the extension request action in TaskHistory
        if is_new:
            for owner in self.task.project.owners.all():
                Notification.objects.create(
                    user=owner.user,
                    message=f"Extension requested for task '{self.task.name}'.",
                    related_task=self.task
                )
            TaskHistory.objects.create(
                task=self.task,
                changed_by=self.requested_by,
                change=f"Extension request for {self.additional_days} days created with reason: {self.reason}"
            )
        elif old_status != self.status:
            TaskHistory.objects.create(
                task=self.task,
                changed_by=self.requested_by,
                change=f"Extension request status changed from {old_status} to {self.status}"
            )

