from django.db import models


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