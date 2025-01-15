from .models import Notification, User, CommunicationPlatform


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
