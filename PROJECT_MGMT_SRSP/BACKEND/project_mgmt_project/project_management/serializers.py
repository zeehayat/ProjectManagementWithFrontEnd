from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    CommunicationPlatform, Project, ProjectOwner, Role,
    UserRoleAssignment, Permission, Notification, UserNotificationPreference, Task, Attachment, TaskExtensionRequest
)


class CommunicationPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationPlatform
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectOwner
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserRoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleAssignment
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class UserNotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationPreference
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'attachments', 'assigned_to', 'project', 'due_date', 'status',
                  'created_at', 'updated_at']

    def validate(self, data):
        # if not data.get("name"):
        #     raise serializers.ValidationError({"name": "This field is required."})
        # if not data.get("assigned_to"):
        #     raise serializers.ValidationError({"assigned_to": "This field is required."})
        # return data
        if not data.get("project"):
            raise serializers.ValidationError({"project": "This field is required."})
        if not data.get("name"):
            raise serializers.ValidationError({"name": "This field is required."})
        return data


class TaskUpdateSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'assigned_to', 'attachments', 'gps_latitude', 'gps_longitude']


class TaskExtensionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExtensionRequest
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


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


class UpdateNotificationPreferencesSerializer(serializers.Serializer):
    platforms = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    def update(self, instance, validated_data):
        platform_ids = validated_data.get("platforms", [])
        for platform_id in platform_ids:
            platform = CommunicationPlatform.objects.get(id=platform_id)
            instance.platforms.add(platform)
        return instance
