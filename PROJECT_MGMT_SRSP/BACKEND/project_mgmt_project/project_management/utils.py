from .models import Notification, User

def create_task_notification(task):
    """
    Creates a notification for the user assigned to the task.
    """
    if task.assigned_to:
        Notification.objects.create(
            user=task.assigned_to,
            message=f"You have been assigned a new task: {task.name}",
            platform=None  # You can set a default platform or handle user preferences
        )
