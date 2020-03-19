from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from pickee_api import api, gateway

app_name = 'pickee_api'


class DefaultNestedRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


# Routers automatically determine the URL conf.
# - Main Router ('api/$')
rootRouter = DefaultNestedRouter()
userRouter = rootRouter.register(r'users', api.PickeeUserViewSet)
rootRouter.register(r'actors', api.ActorViewSet)
rootRouter.register(r'movies', api.MovieViewSet)
rootRouter.register(r'movie-cast', api.MovieCastViewSet)
rootRouter.register(r'genres', api.GenreViewSet)
rootRouter.register(r'recommendations', api.RecommendationViewSet)
rootRouter.register(r'sessions', api.SessionViewSet)

# - Profile Router ('api/profile/$')
userRouter.register(r'favorite-actors',
                    api.FavoriteActorViewSet,
                    basename='favorite-actors',
                    parents_query_lookups=['user'])

userRouter.register(r'favorite-movies',
                    api.FavoriteMovieViewSet,
                    basename='favorite-movies',
                    parents_query_lookups=['user'])

userRouter.register(r'favorite-genres',
                    api.FavoriteGenreViewSet,
                    basename='favorite-genres',
                    parents_query_lookups=['user'])

# Register URLs
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(rootRouter.urls)),
    path('example/', gateway.example_endpoint, name="example"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
