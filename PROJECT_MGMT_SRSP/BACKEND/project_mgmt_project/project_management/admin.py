from django.contrib import admin

from project_management.models.communication_platform import CommunicationPlatform
from project_management.models.notification import Notification
from project_management.models.permission import Permission
from project_management.models.project import Project
from project_management.models.project_owner import ProjectOwner
from project_management.models.role import Role
from project_management.models.user_notification_preferences import UserNotificationPreference
from project_management.models.user_role_assignment import UserRoleAssignment

admin.site.register(CommunicationPlatform)
admin.site.register(Project)
admin.site.register(ProjectOwner)
admin.site.register(Role)
admin.site.register(UserRoleAssignment)
admin.site.register(Permission)
admin.site.register(Notification)
admin.site.register(UserNotificationPreference)
