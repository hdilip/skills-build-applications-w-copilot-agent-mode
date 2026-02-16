from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "calories_burned", "timestamp", "created_at"]
