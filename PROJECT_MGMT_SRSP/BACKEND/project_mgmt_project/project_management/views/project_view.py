from rest_framework.viewsets import ModelViewSet

from project_management.models.project import Project
from project_management.serializers.project_serializer import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    required_role = 'Manager'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer