from rest_framework.routers import DefaultRouter
from .views import (
    CommunicationPlatformViewSet, ProjectViewSet, ProjectOwnerViewSet,
    RoleViewSet, UserRoleAssignmentViewSet, PermissionViewSet,
    NotificationViewSet, UserNotificationPreferenceViewSet
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

urlpatterns = router.urls
