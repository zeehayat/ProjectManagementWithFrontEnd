from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Communication Platforms
class CommunicationPlatform(models.Model):
    name = models.CharField(max_length=255, unique=True)
    api_endpoint = models.TextField(null=True, blank=True)
    config = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_default_in_app():
        platform, created = CommunicationPlatform.objects.get_or_create(name="In-App")
        return platform

    def __str__(self):
        return self.name

# Projects
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Project Owners
class ProjectOwner(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="owners")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

# Roles
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# User Role Assignments
class UserRoleAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

# Permissions
class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    resource = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    platform = models.ForeignKey(CommunicationPlatform, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# User Notification Preferences
class UserNotificationPreference(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="notification_preferences"
    )

    preference_order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    config = models.JSONField(default=dict, blank=True)
    platforms = models.ManyToManyField(CommunicationPlatform, related_name="user_preferences")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.platforms.exists():
            self.platforms.add(CommunicationPlatform.get_default_in_app())


class Attachment(models.Model):
    file = models.FileField(upload_to="attachments/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tasks")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    assignee_notes = models.TextField(blank=True, null=True)
    assigned_person_notes = models.TextField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    attachments = models.ManyToManyField(Attachment, blank=True, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_late(self):
        return self.due_date and self.status != "Completed" and self.due_date < timezone.now().date()
    def __str__(self):
        return self.name


class TaskExtensionRequest(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="extension_requests")
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_days = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=20,
                              choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")],
                              default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)


