from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300, unique=True, blank=False)
    first_name = models.CharField(max_length=36, blank=False)
    last_name = models.CharField(max_length=36, blank=False)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    avatar = models.CharField(max_length=500)

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
        ('UNSPECIFIED', 'Prefer not to say')]
    gender = models.CharField(max_length=18, choices=GENDER_CHOICES)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    associated_users = models.ManyToManyField('self')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class FavoriteActor(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    def __str__(self):
        return self.actor.name


class Actor(models.Model):
    person_id = models.IntegerField()
    name = models.CharField(max_length=128)
    picture = models.ImageField()

    def __str__(self):
        return self.name


class FavoriteMovie(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ": " + self.movie


class Movie(models.Model):
    movie_id = models.IntegerField()
    name = models.CharField(max_length=128)
    picture = models.ImageField()
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    release_date = models.DateField(auto_now=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    def __str__(self):
        return self.actor.name


class FavoriteGenre(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return self.genre.name


class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    USER_CHOICES = [
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('BOOKMARKED', 'Bookmarked')]
    user_choice = models.CharField(max_length=10, choices=USER_CHOICES)

    def __str__(self):
        return self.movie


class Session(models.Model):
    users = models.ManyToManyField('UserProfile')

    def __str__(self):
        return self.id
