from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

from project_management.models.tasks import Task


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    change = models.TextField()

    def __str__(self):
        return f"Change to {self.task.name} at {self.timestamp}"