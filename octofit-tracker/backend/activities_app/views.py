from rest_framework import viewsets, permissions

from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
