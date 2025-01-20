from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from project_management.serializers.create_user_serializer import CreateUserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    #permission_classes = [IsAdminUser]

