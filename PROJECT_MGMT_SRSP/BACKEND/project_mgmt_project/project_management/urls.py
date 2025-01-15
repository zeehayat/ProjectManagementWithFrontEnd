from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    CommunicationPlatformViewSet, ProjectViewSet, ProjectOwnerViewSet,
    RoleViewSet, UserRoleAssignmentViewSet, PermissionViewSet,
    NotificationViewSet, UserNotificationPreferenceViewSet, TaskListCreateView, TaskDetailView,
    RoleListCreateView, UserRoleAssignmentView, NotificationListView, NotificationMarkAsReadView, AddUserView,
    UserListView, CreateUserView, UpdateNotificationPreferences, UserTasksView, TaskUpdateView
)
from .views import ProjectListCreateView, ProjectDetailView

# Define the router
router = DefaultRouter()
router.register(r'communication-platforms', CommunicationPlatformViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-owners', ProjectOwnerViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'user-role-assignments', UserRoleAssignmentViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'user-notification-preferences', UserNotificationPreferenceViewSet)

# Explicit URL patterns
custom_urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('roles/', RoleListCreateView.as_view(), name='roles'),
    path('user-roles/', UserRoleAssignmentView.as_view(), name='user-roles'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:pk>/read/', NotificationMarkAsReadView.as_view(), name='notification-mark-read'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/add/', CreateUserView.as_view(), name='user-create'),
path('update-notifications/', UpdateNotificationPreferences.as_view(), name='update-notifications'),
    path('tasks/user/', UserTasksView.as_view(), name='user-tasks'),
path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),

]

# Combine router and custom paths
urlpatterns = [
    path('', include(router.urls)),  # Router-registered routes
    *custom_urlpatterns,            # Custom routes
]
