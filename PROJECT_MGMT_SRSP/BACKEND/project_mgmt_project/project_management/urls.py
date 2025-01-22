from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views.communication_platform_view import CommunicationPlatformViewSet
from .views.create_user_view import CreateUserView
from .views.dashboard_data_view import DashboardDataView
from .views.logout import LogoutView
from .views.notification_list_view import NotificationListView
from .views.notification_mark_as_read_view import NotificationMarkAsReadView
from .views.notification_view import NotificationViewSet
from .views.project_detail_view import ProjectDetailView
from .views.project_list_create_view import ProjectListCreateView
from .views.project_view import  ProjectViewSet
from .views.project_owner_view import  ProjectOwnerViewSet
from .views.role_list_create_view import RoleListCreateView
from .views.role_view import RoleViewSet
from .views.task_detail_view import TaskDetailView
from .views.task_list_create_view import TaskListCreateView
from .views.task_update_view import TaskUpdateView
from .views.update_notification_preference_view import UpdateNotificationPreferences
from .views.user_list_view import UserListView
from .views.user_notification_preference_view import UserNotificationPreferenceViewSet
from .views.user_role_assignment_view import UserRoleAssignmentViewSet
from .views.permission_view import  PermissionViewSet
from .views.user_task_view import UserTasksView
from .views.user_role_assignment_view import UserRoleAssignment
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
    #path('projects/all/', ProjectViewSet.as_view(), name='project-list-show'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('roles/', RoleListCreateView.as_view(), name='roles'),
    path('user-roles/', UserRoleAssignmentViewSet.as_view({'get':'list','post':'create'}), name='user-roles'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/<int:pk>/read/', NotificationMarkAsReadView.as_view(), name='notification-mark-read'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/add/', CreateUserView.as_view(), name='user-create'),
    path('update-notifications/', UpdateNotificationPreferences.as_view(), name='update-notifications'),
    path('tasks/user/', UserTasksView.as_view(), name='user-tasks'),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("dashboard/", DashboardDataView.as_view(), name="dashboard-data"),
    path('api/logout/', LogoutView.as_view(), name='logout'),

]

# Combine router and custom paths
urlpatterns = [
    path('', include(router.urls)),  # Router-registered routes
    *custom_urlpatterns,            # Custom routes
]
