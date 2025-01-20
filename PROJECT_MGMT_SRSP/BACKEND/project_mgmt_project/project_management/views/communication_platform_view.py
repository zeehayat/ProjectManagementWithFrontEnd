from rest_framework.viewsets import ModelViewSet

from project_management.models.communication_platform import CommunicationPlatform
from project_management.serializers.communication_platform_serializer import CommunicationPlatformSerializer


class CommunicationPlatformViewSet(ModelViewSet):
    queryset = CommunicationPlatform.objects.all()
    serializer_class = CommunicationPlatformSerializer