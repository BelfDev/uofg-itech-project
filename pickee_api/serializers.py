from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

from . import models


class PickeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PickeeUser
        fields = ['id', 'email', 'first_name', 'last_name', 'picture', 'gender', 'age', 'associated_users']


class FavoriteActorSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteActor
        list_serializer_class = BulkListSerializer
        fields = ['id', 'user', 'actor']


class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Actor
        fields = ['id', 'name', 'image_url']


class FavoriteMovieSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteMovie
        list_serializer_class = BulkListSerializer
        fields = ['id', 'user', 'movie']


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Movie
        fields = ['id', 'name', 'image_url', 'rating', 'release_date', 'description']


class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieCast
        fields = ['movie', 'actor']


class FavoriteGenreSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteGenre
        list_serializer_class = BulkListSerializer
        fields = ['id', 'user', 'genre']


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
        fields = ['id', 'users']
