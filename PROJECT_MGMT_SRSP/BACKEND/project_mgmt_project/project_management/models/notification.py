# Notifications
from django.db import models
from django.contrib.auth.models import User

from project_management.models.communication_platform import CommunicationPlatform


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    related_task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name="notifications")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)