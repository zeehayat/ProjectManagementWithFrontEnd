from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from project_management.models.notification import Notification
from project_management.serializers.notification_serializer import NotificationSerializer


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
