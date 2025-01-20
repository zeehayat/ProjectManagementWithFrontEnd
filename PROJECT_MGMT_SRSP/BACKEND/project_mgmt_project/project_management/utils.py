from .models.notification import Notification
from django.contrib.auth.models import User
from .models.communication_platform import  CommunicationPlatform


def create_task_notification(task):
    """
    Creates a notification for the user assigned to the task.
    """
    platform = CommunicationPlatform.get_default_in_app()
    if task.assigned_to:
        Notification.objects.create(
            user=task.assigned_to,
            message=f"You have been assigned a new task: {task.name}",
            platform=platform  # You can set a default platform or handle user preferences
        )

def send_notification(platform, message):
    if platform.name == "Email":
        # Send email logic
        pass
    elif platform.name == "SMS":
        # Send SMS logic
        pass
    elif platform.name == "Slack":
        # Send Slack message logic
        pass
