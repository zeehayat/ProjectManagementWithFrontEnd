
from rest_framework import serializers

from project_management.models.tasks import Task
from project_management.serializers.attachment_serializer import AttachmentSerializer


class TaskSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'attachments', 'assigned_to', 'project', 'due_date', 'status',
                  'created_at', 'updated_at']

    def validate(self, data):

        if not data.get("project"):
            raise serializers.ValidationError({"project": "This field is required."})
        if not data.get("name"):
            raise serializers.ValidationError({"name": "This field is required."})
        return data
