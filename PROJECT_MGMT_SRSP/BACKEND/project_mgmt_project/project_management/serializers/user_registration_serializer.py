from django.contrib.auth.models import User
from rest_framework import serializers

from project_management.models.user_notification_preferences import UserNotificationPreference


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            UserNotificationPreference.objects.create(user=user)
            return user
