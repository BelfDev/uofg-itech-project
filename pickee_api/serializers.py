from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['user', 'email', 'first_name', 'last_name', 'picture', 'avatar', 'gender', 'age', 'associated_users']


class FavoriteActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteActor
        fields = ['user', 'actor']


class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Actor
        fields = ['id', 'name', 'image_url']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteMovie
        fields = ['user', 'movie']


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Movie
        fields = ['id', 'name', 'image_url', 'rating', 'release_date', 'description']


class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieCast
        fields = ['movie', 'actor']


class FavoriteGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteGenre
        fields = ['user', 'genre']


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Genre
        fields = ['id', 'name']


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommendation
        fields = ['movie', 'session', 'user_choice']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = ['users']

