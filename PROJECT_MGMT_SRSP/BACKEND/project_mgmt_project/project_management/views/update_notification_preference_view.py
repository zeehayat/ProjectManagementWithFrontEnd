from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from project_management.models.user_notification_preferences import UserNotificationPreference
from project_management.serializers.update_notification_preference_serializer import \
    UpdateNotificationPreferencesSerializer


class UpdateNotificationPreferences(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            preferences = user.notification_preferences
        except UserNotificationPreference.DoesNotExist:
            return Response({"detail": "User has no notification preferences."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UpdateNotificationPreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(preferences, serializer.validated_data)
            return Response({"detail": "Notification preferences updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
