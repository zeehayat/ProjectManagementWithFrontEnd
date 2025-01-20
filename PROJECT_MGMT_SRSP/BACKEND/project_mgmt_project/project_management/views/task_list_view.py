from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from project_management.models.tasks import Task
from project_management.serializers.task_serializer import TaskSerializer


class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.all()
