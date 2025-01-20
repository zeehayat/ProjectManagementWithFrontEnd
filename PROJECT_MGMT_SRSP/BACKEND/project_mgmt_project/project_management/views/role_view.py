from rest_framework.viewsets import ModelViewSet

from project_management.models.role import Role
from project_management.serializers.role_serializer import RoleSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer