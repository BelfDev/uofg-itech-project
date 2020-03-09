from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user.first_name.blank = False
    user.last_name.blank = False

    picture = models.ImageField(upload_to='profile_images', blank=True)

    GENDER_CHOICES = ('Male', 'Female', 'Other', 'Prefer not to say')
    gender = models.CharField(max_length=18, choices=GENDER_CHOICES)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    associated_users = models.ManyToManyField("self")

    favourite_actors = models.ManyToManyField(Actor, symmetrical=False)
    favourite_movies = models.ManyToManyField(Movie, symmetrical=False)
    favourite_genres = models.ManyToManyField(Genre, symmetrical=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Actor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField()
    #need some way to retrieve from an API

class Movie(models.Model):
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField()
    #need some way to retrieve from an API

class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #need some way to retrieve from an API