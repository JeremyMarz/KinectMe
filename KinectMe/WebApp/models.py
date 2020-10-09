from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activities(models.Model):
    ACTIVITY= (
        ("Climbing", "Climbing"),
        ("Soccer", "Soccer"),
        ("Football", "Football"),
        ("Ultimate Frisbee", "Ultimate Frisbee"),
        ("Yoga", "Yoga"),
        ("Running", "Running"),
        ("Basketball", "Basketball"),
        ("Vollyball", "Vollyball"),
        ("Cycling", "Cycling"),
        ("Golf", "Golf"),
        ("Cornhole", "Cornhole"),
        ("Baseball", "Baseball"),
        ("Softball", "Softball"),
        ("Zumba", "Zumba"),
        ("Lifing", "Lifting"),
        ("Cricket", "Cricket"),
        ("Tennis", "Tennis"),
        ("Spikeball", "Spikeball"),
        ("Other", "Other"),
)
    sport = models.CharField(max_length=20, unique=True, choices=ACTIVITY)
    def __str__(self):
        return self.sport

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    sport = models.ManyToManyField(Activities)


    def __str__(self):
        return self.user_name

class Event(models.Model):
    organizer = models.OneToOneField(Profile,on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=20)
    sport = models.OneToOneField(Activities, on_delete=models.CASCADE, null=False)
