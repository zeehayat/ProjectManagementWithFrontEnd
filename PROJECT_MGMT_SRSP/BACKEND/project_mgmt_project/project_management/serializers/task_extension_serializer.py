from rest_framework import serializers

from project_management.models.task_extension_request import TaskExtensionRequest


class TaskExtensionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExtensionRequest
        fields = "__all__"