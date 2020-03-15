from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from pickee_api.managers import PickeeUserManager


class PickeeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PickeeUserManager()

    class Meta:
        verbose_name = 'user'

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(PickeeUser, on_delete=models.CASCADE)
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
    associated_users = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return str(self.user.username)


class FavoriteActor(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    def __str__(self):
        return self.actor.name


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class FavoriteMovie(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ": " + self.movie


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    image_url = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 validators=[MaxValueValidator(10.0), MinValueValidator(0)])
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
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, default=None)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return self.genre.name


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
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
    user_choice = models.CharField(max_length=10, choices=USER_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Session(models.Model):
    users = models.ManyToManyField(UserProfile)

    def __str__(self):
        return str(self.id)
