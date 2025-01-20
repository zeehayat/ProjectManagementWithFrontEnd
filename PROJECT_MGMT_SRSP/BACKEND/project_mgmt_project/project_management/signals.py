from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.tasks import Task
from .models.user_notification_preferences import UserNotificationPreference
from .models.communication_platform import  CommunicationPlatform
from .utils import create_task_notification
from django.contrib.auth.models import User
@receiver(post_save, sender=Task)
def task_assignment_notification(sender, instance, created, **kwargs):
    """
    Sends a notification when a task is assigned.
    """
    if created:  # Trigger only when a new task is created
        create_task_notification(instance)

@receiver(post_save, sender=User)
def create_user_notification_preferences(sender, instance, created, **kwargs):
    if created:
        preference = UserNotificationPreference.objects.create(user=instance)
        # Add default in-app platform
        preference.platforms.add(CommunicationPlatform.get_default_in_app())