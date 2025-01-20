from rest_framework.viewsets import ModelViewSet

from project_management.models.user_role_assignment import UserRoleAssignment
from project_management.serializers.user_role_assignment_serializer import UserRoleAssignmentSerializer


class UserRoleAssignmentViewSet(ModelViewSet):
    queryset = UserRoleAssignment.objects.all()
    serializer_class = UserRoleAssignmentSerializer
