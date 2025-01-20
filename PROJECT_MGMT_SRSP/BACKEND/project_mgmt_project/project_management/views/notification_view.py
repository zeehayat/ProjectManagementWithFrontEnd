from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from project_management.models.notification import Notification
from project_management.permissions import HasPermission
from project_management.serializers.notification_serializer import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasPermission]
    required_permission = 'send_notification'
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer