from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from project_management.models.tasks import Task
from project_management.serializers.task_serializer import TaskSerializer


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset