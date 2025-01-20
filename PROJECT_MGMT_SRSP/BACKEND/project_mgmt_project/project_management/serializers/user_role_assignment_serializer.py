from rest_framework import serializers

from project_management.models.user_role_assignment import UserRoleAssignment


class UserRoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleAssignment
        fields = '__all__'
