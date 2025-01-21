from rest_framework import serializers

from project_management.models.attachment import Attachment
from project_management.models.notification import Notification
from project_management.models.tasks import Task


class TaskUpdateSerializer(serializers.ModelSerializer):
    attachments = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )
    remove_attachments = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Task
        fields = ["status", "assignee_notes", "assigned_person_notes", "attachments", "remove_attachments"]

    def update(self, instance, validated_data):
        # Handle adding attachments
        changes = []

        attachments = validated_data.pop("attachments", [])
        if attachments:
            for attachment in attachments:
                attachment_instance = Attachment.objects.create(file=attachment)
                instance.attachments.add(attachment_instance)
            changes.append("attachments added")

        # Handle removing attachments
        remove_attachments = validated_data.pop("remove_attachments", [])
        for attachment_id in remove_attachments:
            attachment_instance = Attachment.objects.filter(id=attachment_id).first()
            if attachment_instance:
                instance.attachments.remove(attachment_instance)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        self.notify_assigner(instance, changes)

        return instance

    def validate_attachments(self, value):
        for file in value:
            if file.size > 10 * 1024 * 1024:  # Limit to 10 MB
                raise serializers.ValidationError(f"File {file.name} exceeds the size limit of 10MB.")
        return value

    def notify_assigner(instance, changes):
        if instance.project.owners.exists():
            assigner = instance.project.owners.first().user
            Notification.objects.create(
                user=assigner,
                message=f"The task '{instance.name}' was updated: {', '.join(changes)}."
            )
