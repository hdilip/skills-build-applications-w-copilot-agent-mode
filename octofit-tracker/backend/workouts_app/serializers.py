from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "user", "name", "description", "duration_minutes", "calories_burned", "created_at"]
