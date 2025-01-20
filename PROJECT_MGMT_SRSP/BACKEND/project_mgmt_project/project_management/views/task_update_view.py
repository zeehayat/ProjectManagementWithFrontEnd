from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from project_management.models.tasks import Task
from project_management.serializers.task_update_serializer import TaskUpdateSerializer
from project_management.views.is_task_assigned_view import IsTaskAssignee


class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsTaskAssignee]
    parser_classes = [MultiPartParser, FormParser]

    def patch(self, request, pk):
        # print("Request Data:", request.data)  # Debug incoming data
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskUpdateSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                #print("Validated Data:", serializer.validated_data)  # Debug validated data
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)