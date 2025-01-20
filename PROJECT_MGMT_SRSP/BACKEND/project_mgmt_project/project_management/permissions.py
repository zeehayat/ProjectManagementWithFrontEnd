from rest_framework.permissions import BasePermission
from .models.user_role_assignment import UserRoleAssignment
from rest_framework.permissions import BasePermission


class IsRoleAuthorized(BasePermission):
    """
    Custom permission to allow access based on user roles.
    """

    def has_permission(self, request, view):
        # Example: Restrict access to users with the 'Manager' role
        required_role = getattr(view, 'required_role', None)
        if not required_role:
            return True  # No specific role required; allow access

        # Check if the user is assigned the required role
        user_roles = UserRoleAssignment.objects.filter(user=request.user).values_list('role__name', flat=True)
        return required_role in user_roles

class HasPermission(BasePermission):
    """
    Custom permission to allow access based on specific user permissions.
    """
    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        if not required_permission:
            return True  # No specific permission required; allow access

        # Check if the user has the required permission
        user_permissions = request.user.userroleassignment_set.filter(
            role__permissions__name=required_permission
        ).values_list('role__permissions__name', flat=True)
        return required_permission in user_permissions
