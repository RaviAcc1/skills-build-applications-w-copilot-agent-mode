from django.test import TestCase
from .models import UserProfile, Activity, Team, Leaderboard, Workout

class UserProfileTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(name="Test User", email="test@example.com")

    def test_userprofile_created(self):
        user = UserProfile.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Test Team", members=["test@example.com"])

    def test_team_created(self):
        team = Team.objects.get(name="Test Team")
        self.assertIn("test@example.com", team.members)

class ActivityTestCase(TestCase):
    def setUp(self):
        user = UserProfile.objects.create(name="Test User", email="test@example.com")
        Activity.objects.create(user=user, activity_type="Running", duration_minutes=30, date="2025-12-10T00:00:00Z")

    def test_activity_created(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration_minutes, 30)

class LeaderboardTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Test Team", members=["test@example.com"])
        Leaderboard.objects.create(team=team, points=100)

    def test_leaderboard_created(self):
        leaderboard = Leaderboard.objects.get(team__name="Test Team")
        self.assertEqual(leaderboard.points, 100)

class WorkoutTestCase(TestCase):
    def setUp(self):
        Workout.objects.create(name="Test Workout", description="A test workout", duration_minutes=60)

    def test_workout_created(self):
        workout = Workout.objects.get(name="Test Workout")
        self.assertEqual(workout.duration_minutes, 60)
