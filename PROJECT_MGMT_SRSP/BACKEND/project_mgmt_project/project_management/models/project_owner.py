from django.db import models
from django.contrib.auth.models import User
from project_management.models.project import Project


# Project Owners
class ProjectOwner(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="owners")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
