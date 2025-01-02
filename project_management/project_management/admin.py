from django.contrib import admin
from .models import (
    CommunicationPlatform, Project, ProjectOwner, Role, UserRoleAssignment,
    Permission, Notification, UserNotificationPreference
)

admin.site.register(CommunicationPlatform)
admin.site.register(Project)
admin.site.register(ProjectOwner)
admin.site.register(Role)
admin.site.register(UserRoleAssignment)
admin.site.register(Permission)
admin.site.register(Notification)
admin.site.register(UserNotificationPreference)
