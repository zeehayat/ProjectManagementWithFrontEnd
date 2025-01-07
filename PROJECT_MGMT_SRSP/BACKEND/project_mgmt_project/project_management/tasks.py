from celery import shared_task
from .models import Task
from .models import Notification

@shared_task
def check_late_tasks():
    from django.utils.timezone import now
    late_tasks = Task.objects.filter(status__in=["Pending", "In Progress"], due_date__lt=now().date())
    for task in late_tasks:
        Notification.objects.create(
            user=task.assigned_to,
            message=f"The task '{task.name}' is running late!"
        )
