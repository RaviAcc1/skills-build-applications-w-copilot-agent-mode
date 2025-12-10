from rest_framework import viewsets
from .models import UserProfile, Activity, Team
from .serializers import UserProfileSerializer, ActivitySerializer, TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


from .models import Leaderboard, Workout
from .serializers import LeaderboardSerializer, WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
