

from rest_framework import serializers

from project_management.models.attachment import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
