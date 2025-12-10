from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ActivityViewSet, TeamViewSet, LeaderboardViewSet, WorkoutViewSet

router = DefaultRouter()

router.register(r'users', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('userprofile-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'leaderboards': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
