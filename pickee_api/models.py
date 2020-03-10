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

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class FavouriteActors(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField()
    #need some way to retrieve from an API

class FavouriteMovies(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField()
    #need some way to retrieve from an API

class FavouriteGenres(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    #need some way to retrieve from an API