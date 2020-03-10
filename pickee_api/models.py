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
    associated_users = models.ManyToManyField('self')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class FavouriteActors(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField()
    #need some way to retrieve from an API

    def __str__(self):
        return self.name

class FavouriteMovies(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ": " + self.movie

class FavouriteGenres(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    #need some way to retrieve from an API

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=128)
    picture = models.ImageField()
    #need some way to retrieve from an API

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    USER_CHOICES = ('Accepted', 'Rejected', 'Bookmarked')
    user_choice = models.CharField(max_length=10, choices=USER_CHOICES)

    def __str__(self):
        return self.movie

class Session(models.Model):
    users = models.ManyToManyField('UserProfile')

    def __str__(self):
        return self.id