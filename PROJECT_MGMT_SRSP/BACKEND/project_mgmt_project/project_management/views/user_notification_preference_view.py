from rest_framework.viewsets import ModelViewSet

from project_management.models.user_notification_preferences import UserNotificationPreference
from project_management.serializers.user_notification_preference_serializer import UserNotificationPreferenceSerializer


class UserNotificationPreferenceViewSet(ModelViewSet):
    queryset = UserNotificationPreference.objects.all()
    serializer_class = UserNotificationPreferenceSerializer
