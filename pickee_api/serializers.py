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
    class Meta:
        model = models.Actor
        fields = ['person_id', 'name', 'picture']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    model = models.FavoriteMovie
    fields = ['user', 'movie']


class MovieSerializer(serializers.ModelSerializer):
    model = models.Movie
    fields = ['movie_id', 'name', 'picture', 'rating', 'release_date', 'description']


class MovieCastSerializer(serializers.ModelSerializer):
    model = models.MovieCast
    fields = ['movie', 'actor']


class FavoriteGenreSerializer(serializers.ModelSerializer):
    model = models.FavoriteGenre
    fields = ['user', 'genre']


class GenreSerializer(serializers.ModelSerializer):
    model = models.Genre
    fields = ['genre_id', 'name']


class RecommendationSerializer(serializers.ModelSerializer):
    model = models.Recommendation
    fields = ['movie', 'session', 'user_choice']


class SessionSerializer(serializers.ModelSerializer):
    model = models.Session
    fields = ['users']
