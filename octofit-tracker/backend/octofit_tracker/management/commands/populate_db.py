from django.core.management.base import BaseCommand
from tracker.models import UserProfile, Activity, Team
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()

        # Create users
        marvel = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com'},
            {'name': 'Captain America', 'email': 'cap@marvel.com'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com'},
        ]
        dc = [
            {'name': 'Batman', 'email': 'batman@dc.com'},
            {'name': 'Superman', 'email': 'superman@dc.com'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [UserProfile.objects.create(**u) for u in marvel]
        dc_users = [UserProfile.objects.create(**u) for u in dc]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', members=[u.email for u in marvel_users])
        dc_team = Team.objects.create(name='DC', members=[u.email for u in dc_users])

        # Create activities
        for user in marvel_users + dc_users:
            Activity.objects.create(
                user=user,
                activity_type='Running',
                duration_minutes=30,
                date=timezone.now()
            )
            Activity.objects.create(
                user=user,
                activity_type='Cycling',
                duration_minutes=45,
                date=timezone.now()
            )
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
