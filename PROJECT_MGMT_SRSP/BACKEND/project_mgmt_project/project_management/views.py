from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .permissions import HasPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import (
    CommunicationPlatform, Project, ProjectOwner, Role,
    UserRoleAssignment, Permission, Notification, UserNotificationPreference, Task
)
from .serializers import (
    CommunicationPlatformSerializer, ProjectSerializer, ProjectOwnerSerializer,
    RoleSerializer, UserRoleAssignmentSerializer, PermissionSerializer,
    NotificationSerializer, UserNotificationPreferenceSerializer, TaskSerializer
)
from .utils import create_task_notification


class CommunicationPlatformViewSet(ModelViewSet):
    queryset = CommunicationPlatform.objects.all()
    serializer_class = CommunicationPlatformSerializer


class ProjectViewSet(ModelViewSet):
    required_role = 'Manager'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectOwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjectOwner.objects.all()
    serializer_class = ProjectOwnerSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleAssignmentViewSet(ModelViewSet):
    queryset = UserRoleAssignment.objects.all()
    serializer_class = UserRoleAssignmentSerializer


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class NotificationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasPermission]
    required_permission = 'send_notification'
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserNotificationPreferenceViewSet(ModelViewSet):
    queryset = UserNotificationPreference.objects.all()
    serializer_class = UserNotificationPreferenceSerializer


class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"error": "Project Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"error": "Project Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({"error": "Project Not Found"}, status=status.HTTP_404_NOT_FOUND)


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            create_task_notification(task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


class RoleListCreateView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# Assign Roles to Users
class UserRoleAssignmentView(ListCreateAPIView):
    queryset = UserRoleAssignment.objects.all()
    serializer_class = UserRoleAssignmentSerializer


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


# Mark Notification as Read
class NotificationMarkAsReadView(UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, is_read=False)
