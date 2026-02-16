from django.db import models
from django.conf import settings


class Activity(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	distance_km = models.FloatField(null=True, blank=True)
	calories_burned = models.PositiveIntegerField(null=True, blank=True)
	timestamp = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.activity_type} by {self.user}"
