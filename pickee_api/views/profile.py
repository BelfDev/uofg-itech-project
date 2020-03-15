from rest_framework import viewsets
from pickee_api import models, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class FavoriteActorViewSet(viewsets.ModelViewSet):
    queryset = models.FavoriteActor.objects.all()
    serializer_class = serializers.FavoriteActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = models.FavoriteMovie.objects.all()
    serializer_class = serializers.FavoriteMovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieCastViewSet(viewsets.ModelViewSet):
    queryset = models.MovieCast.objects.all()
    serializer_class = serializers.MovieCastSerializer


class FavoriteGenreViewSet(viewsets.ModelViewSet):
    queryset = models.FavoriteGenre.objects.all
    serializer_class = serializers.FavoriteGenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer

