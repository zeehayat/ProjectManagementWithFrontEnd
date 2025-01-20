from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from project_management.models.task_extension_request import TaskExtensionRequest
from project_management.serializers.task_extension_serializer import TaskExtensionRequestSerializer


class TaskExtensionRequestApprovalView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, request_id):
        try:
            extension_request = TaskExtensionRequest.objects.get(pk=request_id)
            serializer = TaskExtensionRequestSerializer(extension_request, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskExtensionRequest.DoesNotExist:
            return Response({"detail": "Extension request not found."}, status=status.HTTP_404_NOT_FOUND)
