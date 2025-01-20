from rest_framework.generics import ListCreateAPIView

from project_management.models.role import Role
from project_management.serializers.role_serializer import RoleSerializer


class RoleListCreateView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
