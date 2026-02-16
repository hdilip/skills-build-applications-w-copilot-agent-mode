from django.core.management.base import BaseCommand
from users_app.models import User
from activities_app.models import Activity
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            User.objects.all().delete()
            Activity.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel_team = 'Marvel'
            dc_team = 'DC'

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User(email='ironman@marvel.com', username='IronMan', team=marvel_team),
                User(email='captain@marvel.com', username='CaptainAmerica', team=marvel_team),
                User(email='batman@dc.com', username='Batman', team=dc_team),
                User(email='superman@dc.com', username='Superman', team=dc_team),
            ]
            User.objects.bulk_create(users)

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            activities = [
                Activity(user=users[0], type='Run', duration=30, calories=300),
                Activity(user=users[1], type='Swim', duration=45, calories=400),
                Activity(user=users[2], type='Bike', duration=60, calories=500),
                Activity(user=users[3], type='Yoga', duration=50, calories=200),
            ]
            Activity.objects.bulk_create(activities)

            self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
