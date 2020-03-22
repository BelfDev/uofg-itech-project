from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from pickee_api.managers import PickeeUserManager


class PickeeUser(AbstractBaseUser, PermissionsMixin):
    # id = models.AutoField(primary_key=True)
    # Required field
    email = models.EmailField(_('email address'), unique=True)

    # Pre-populated fields
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Optional fields (profile)
    first_name = models.CharField(max_length=36, blank=True)
    last_name = models.CharField(max_length=36, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], blank=True, null=True)

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
        ('UNSPECIFIED', 'Prefer not to say')]
    gender = models.CharField(max_length=18, choices=GENDER_CHOICES, blank=True, null=True)

    associated_users = models.ManyToManyField('self', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PickeeUserManager()

    class Meta:
        verbose_name = 'user'

    def __str__(self):
        return self.email


class FavoriteActor(models.Model):
    user = models.ForeignKey('PickeeUser', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'actor')

    def __str__(self):
        return self.user.email + ": " + self.actor.name


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class FavoriteMovie(models.Model):
    user = models.ForeignKey('PickeeUser', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return self.movie.name


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    image_url = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 validators=[MaxValueValidator(10.0), MinValueValidator(0)])
    release_date = models.DateField(auto_now=False, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    def __str__(self):
        return self.actor.name


class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=128)

    def __str__(self):
        return self.keyword


class MovieKeyword(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + ': ' + self.keyword.keyword


class FavoriteGenre(models.Model):
    user = models.ForeignKey('PickeeUser', on_delete=models.CASCADE, default=None)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'genre')

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
    users = models.ManyToManyField(PickeeUser)

    def __str__(self):
        return str(self.id)
