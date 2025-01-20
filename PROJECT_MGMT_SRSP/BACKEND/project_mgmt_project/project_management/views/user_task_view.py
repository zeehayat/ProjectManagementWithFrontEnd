from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project_management.models.project_owner import ProjectOwner
from project_management.models.tasks import Task
from project_management.serializers.task_serializer import TaskSerializer


class UserTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Get all projects the user owns
        owned_projects = ProjectOwner.objects.filter(user=user).values_list("project", flat=True)

        # Tasks assigned to the user
        assigned_to_user = Task.objects.filter(assigned_to=user).select_related("project")

        # Tasks from projects owned by the user
        assigned_by_user = Task.objects.filter(project__in=owned_projects).select_related("project")

        # Group tasks by project
        grouped_tasks = {}
        for task in assigned_to_user.union(assigned_by_user):
            project_name = task.project.name
            if project_name not in grouped_tasks:
                grouped_tasks[project_name] = []
            grouped_tasks[project_name].append(TaskSerializer(task).data)

        return Response(grouped_tasks)
