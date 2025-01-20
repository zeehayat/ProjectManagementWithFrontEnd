from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from project_management.serializers.user_serializier import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # For listing users (without passwords)
