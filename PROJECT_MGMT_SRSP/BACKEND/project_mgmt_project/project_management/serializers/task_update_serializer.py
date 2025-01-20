from rest_framework import serializers

from project_management.models.attachment import Attachment
from project_management.models.tasks import Task


class TaskUpdateSerializer(serializers.ModelSerializer):
    attachments = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )

    class Meta:
        model = Task
        fields = ["status", "assignee_notes", "assigned_person_notes", "attachments"]

    def update(self, instance, validated_data):
        # Handle attachments separately
        attachments = validated_data.pop("attachments", [])
        for attachment in attachments:
            attachment_instance = Attachment.objects.create(file=attachment)
            instance.attachments.add(attachment_instance)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


