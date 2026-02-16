from rest_framework import viewsets, permissions
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
