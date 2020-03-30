from django.urls import include, path
from rest_framework_bulk.routes import BulkRouter
from rest_framework_extensions.routers import NestedRouterMixin

from pickee_api import api, gateway

app_name = 'pickee_api'


class DefaultNestedRouter(NestedRouterMixin, BulkRouter):
    """
               Custom router to register nested API resources
    """
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
    path('search/actors/', gateway.search_actors, name="search-actors"),
    path('search/movies/', gateway.search_movies, name="search-movies"),
    path('recommendations/generate', gateway.generate_recommendation, name="generate-recommendation"),
    path('providers/', gateway.get_available_providers, name="providers")
]
