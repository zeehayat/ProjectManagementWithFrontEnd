from django.db import models


from project_management.models.role import Role


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    resource = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)