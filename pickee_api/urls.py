from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from pickee_api.views import auth, profile, recommendation

app_name = 'pickee_api'


class DefaultNestedRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


# Routers automatically determine the URL conf.
# - Main Router ('api/$')
rootRouter = DefaultNestedRouter()
rootRouter.register(r'users', auth.PickeeUserViewSet)
rootRouter.register(r'actors', profile.ActorViewSet)
rootRouter.register(r'movies', profile.MovieViewSet)
rootRouter.register(r'movie-cast', profile.MovieCastViewSet)
rootRouter.register(r'genres', profile.GenreViewSet)
rootRouter.register(r'recommendations', recommendation.RecommendationViewSet)
rootRouter.register(r'sessions', recommendation.SessionViewSet)

profileRouter = rootRouter.register(r'profiles', profile.UserProfileViewSet)

# - Profile Router ('api/profile/$')
profileRouter.register(r'favorite-actors',
                       profile.FavoriteActorViewSet,
                       basename='favorite-actors',
                       parents_query_lookups=['user'])

profileRouter.register(r'favorite-movies',
                       profile.FavoriteMovieViewSet,
                       basename='favorite-movies',
                       parents_query_lookups=['user'])

profileRouter.register(r'favorite-genres',
                       profile.FavoriteGenreViewSet,
                       basename='favorite-genres',
                       parents_query_lookups=['user'])

# Register URLs
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(rootRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
