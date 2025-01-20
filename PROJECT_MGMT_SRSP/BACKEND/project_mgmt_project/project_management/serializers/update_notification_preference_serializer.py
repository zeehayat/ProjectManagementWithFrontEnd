from rest_framework import serializers

from project_management.models.communication_platform import CommunicationPlatform


class UpdateNotificationPreferencesSerializer(serializers.Serializer):
    platforms = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    def update(self, instance, validated_data):
        platform_ids = validated_data.get("platforms", [])
        for platform_id in platform_ids:
            try:
                platform = CommunicationPlatform.objects.get(id=platform_id)
                instance.platforms.add(platform)  # Use the RelatedManager's add() method
            except CommunicationPlatform.DoesNotExist:
                raise serializers.ValidationError(
                    {"platforms": f"Platform with ID {platform_id} does not exist."}
                )
            return instance
