from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .utils import create_task_notification

@receiver(post_save, sender=Task)
def task_assignment_notification(sender, instance, created, **kwargs):
    """
    Sends a notification when a task is assigned.
    """
    if created:  # Trigger only when a new task is created
        create_task_notification(instance)