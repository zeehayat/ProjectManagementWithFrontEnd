from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from project_management.models.project_owner import ProjectOwner
from project_management.serializers.project_owner_serializer import ProjectOwnerSerializer


class ProjectOwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjectOwner.objects.all()
    serializer_class = ProjectOwnerSerializer