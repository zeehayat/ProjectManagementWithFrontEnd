from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from project_management.models.project import Project
from project_management.models.tasks import Task


class DashboardDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Task Summary
        task_summary = {
            "pending": Task.objects.filter(status="Pending", assigned_to=user).count(),
            "in_progress": Task.objects.filter(status="In Progress", assigned_to=user).count(),
            "completed": Task.objects.filter(status="Completed", assigned_to=user).count(),
        }

        # Project Summary
        projects = Project.objects.filter(owners__user=user).distinct()
        project_summary = {
            "total_projects": projects.count(),
            "recent_projects": [
                {"name": project.name, "updated_at": project.updated_at} for project in projects.order_by("-updated_at")[:5]
            ],
        }

        # Notifications
        overdue_tasks = Task.objects.filter(
            due_date__lt=timezone.now(),
            status__in=["Pending", "In Progress"],
            assigned_to=user,
        ).select_related("assigned_to")

        # Add "assigned_to" field with conditional formatting
        overdue_task_data = [
            {
                "name": task.name,
                "due_date": task.due_date,
                "assigned_to": "Assigned to me" if task.assigned_to == user else task.assigned_to.username,
            }
            for task in overdue_tasks
        ]

        return Response({
            "task_summary": task_summary,
            "project_summary": project_summary,
            "overdue_tasks": overdue_task_data,
        })