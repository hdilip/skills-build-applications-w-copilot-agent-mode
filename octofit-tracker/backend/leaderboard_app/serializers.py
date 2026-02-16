from rest_framework import serializers
from .models import LeaderboardEntry

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ["id", "user", "team", "score", "rank", "updated_at"]
