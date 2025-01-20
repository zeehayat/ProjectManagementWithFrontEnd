from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

from project_management.models.communication_platform import CommunicationPlatform


class UserNotificationPreference(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="notification_preferences"
    )

    preference_order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    config = models.JSONField(default=dict, blank=True)
    platforms = models.ManyToManyField(CommunicationPlatform, related_name="user_preferences")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.platforms.exists():
            self.platforms.add(CommunicationPlatform.get_default_in_app())
