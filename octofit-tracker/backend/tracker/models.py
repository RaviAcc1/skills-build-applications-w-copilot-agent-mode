from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.activity_type} - {self.user.email}"


class Team(models.Model):
    name = models.CharField(max_length=140)
    members = models.JSONField(default=list)


    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - {self.points} pts"


class Workout(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
