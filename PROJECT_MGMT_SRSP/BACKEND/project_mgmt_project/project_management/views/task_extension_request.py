from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from project_management.models.tasks import Task
from project_management.serializers.task_extension_serializer import TaskExtensionRequestSerializer


class TaskExtensionRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            data = request.data
            data['task'] = task.id
            data['requested_by'] = request.user.id
            serializer = TaskExtensionRequestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
