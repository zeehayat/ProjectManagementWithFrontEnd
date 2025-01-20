from project_management.models.project_owner import ProjectOwner
from rest_framework import serializers

class ProjectOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectOwner
        fields = '__all__'
