from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from project_management.models.notification import Notification
from project_management.serializers.notification_serializer import NotificationSerializer


class NotificationMarkAsReadView(UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, is_read=False)
