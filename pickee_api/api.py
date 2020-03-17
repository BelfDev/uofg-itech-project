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
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteMovieViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.FavoriteMovie.objects.all()
    serializer_class = serializers.FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieCastViewSet(viewsets.ModelViewSet):
    queryset = models.MovieCast.objects.all()
    serializer_class = serializers.MovieCastSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteGenreViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.FavoriteGenre.objects.all()
    serializer_class = serializers.FavoriteGenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

class PreviousRecommendationViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        session_set = models.Session.objects.all()
        email = self.request.query_params.get('email')
        user = PickeeUser.objects.get(email=email)
        session_set.filter(users=user)

        recommendation_set = models.Recommendation.objects.all()
        recommendation_set.filter(session=session_set)
        return recommendation_set
        
    