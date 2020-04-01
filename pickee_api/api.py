from rest_framework import viewsets, permissions, renderers
from rest_framework_bulk import BulkModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from pickee_api import models, serializers
from pickee_api.models import PickeeUser
from pickee_api.serializers import PickeeUserSerializer


# Create internal application endpoints

class PickeeUserViewSet(viewsets.ModelViewSet):
    """
            A Django Rest Framework (DRF) ViewSet that reprents a PickeeUser.
            This composition allows default REST operations to be set up automatically.
    """
    renderer_classes = [renderers.JSONRenderer]
    queryset = PickeeUser.objects.all().order_by('-date_joined')
    serializer_class = PickeeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
                Optionally restricts the returned users to a given user,
                by filtering against a `email` query parameter in the URL.
        """
        queryset = PickeeUser.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset


class FavoriteActorViewSet(NestedViewSetMixin, BulkModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.FavoriteActor.objects.all()
    serializer_class = serializers.FavoriteActorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteMovieViewSet(NestedViewSetMixin, BulkModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.FavoriteMovie.objects.all()
    serializer_class = serializers.FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieCastViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.MovieCast.objects.all()
    serializer_class = serializers.MovieCastSerializer
    permission_classes = [permissions.IsAuthenticated]


class FavoriteGenreViewSet(NestedViewSetMixin, BulkModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.FavoriteGenre.objects.all()
    serializer_class = serializers.FavoriteGenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class RecommendationViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PreviousRecommendationViewSet(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    session_set = models.Session.objects.all()
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Supports finding recommendations via email query parameter
        session_set = models.Session.objects.all()
        queryset = models.Recommendation.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            session_set = session_set.filter(email=email)
            queryset = queryset.filter(session__in=session_set)
        return queryset
