from rest_framework import viewsets, permissions
from rest_framework_extensions.mixins import NestedViewSetMixin

from pickee_api import models, serializers
from pickee_api.models import PickeeUser
from pickee_api.serializers import PickeeUserSerializer


class PickeeUserViewSet(viewsets.ModelViewSet):
    queryset = PickeeUser.objects.all().order_by('-date_joined')
    serializer_class = PickeeUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteActorViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.FavoriteActor.objects.all()
    serializer_class = serializers.FavoriteActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteMovieViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.FavoriteMovie.objects.all()
    serializer_class = serializers.FavoriteMovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieCastViewSet(viewsets.ModelViewSet):
    queryset = models.MovieCast.objects.all()
    serializer_class = serializers.MovieCastSerializer


class FavoriteGenreViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.FavoriteGenre.objects.all()
    serializer_class = serializers.FavoriteGenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
