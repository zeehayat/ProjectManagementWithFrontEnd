from project_management.models.communication_platform import CommunicationPlatform
from rest_framework import serializers

class CommunicationPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationPlatform
        fields = '__all__'
