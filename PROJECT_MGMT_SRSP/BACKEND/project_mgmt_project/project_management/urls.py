from rest_framework.routers import DefaultRouter
from .views import (
    CommunicationPlatformViewSet, ProjectViewSet, ProjectOwnerViewSet,
    RoleViewSet, UserRoleAssignmentViewSet, PermissionViewSet,
    NotificationViewSet, UserNotificationPreferenceViewSet, TaskListCreateView, TaskDetailView
)

router = DefaultRouter()
router.register(r'communication-platforms', CommunicationPlatformViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-owners', ProjectOwnerViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'user-role-assignments', UserRoleAssignmentViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'user-notification-preferences', UserNotificationPreferenceViewSet)
from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

urlpatterns = router.urls
