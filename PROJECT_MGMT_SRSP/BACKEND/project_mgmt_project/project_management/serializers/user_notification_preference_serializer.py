from rest_framework import serializers

from project_management.models.user_notification_preferences import UserNotificationPreference


class UserNotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationPreference
        fields = '__all__'