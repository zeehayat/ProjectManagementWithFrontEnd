from rest_framework.viewsets import ModelViewSet

from project_management.models.permission import Permission
from project_management.serializers.permission_serializer import PermissionSerializer


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
