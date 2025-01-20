from django.db import models
from django.contrib.auth.models import User


from project_management.models.project import Project
from project_management.models.role import Role


# User Role Assignments
class UserRoleAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)