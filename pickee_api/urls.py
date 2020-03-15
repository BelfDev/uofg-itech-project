from django.urls import include, path
from rest_framework import routers

from pickee_api.views import auth, profile, recommendation

app_name = 'pickee_api'

# Routers provide an easy way of automatically determining the URL conf.
# - Main Router ('api/$')
rootRouter = routers.DefaultRouter()
rootRouter.register(r'users', auth.UserViewSet)
rootRouter.register(r'profiles', profile.UserProfileViewSet)
rootRouter.register(r'actors', profile.ActorViewSet)
rootRouter.register(r'movies', profile.MovieViewSet)
rootRouter.register(r'movie-cast', profile.MovieCastViewSet)
rootRouter.register(r'genres', profile.GenreViewSet)
rootRouter.register(r'recommendations', recommendation.RecommendationViewSet)
rootRouter.register(r'sessions', recommendation.SessionViewSet)

# TODO: Finish the nested routes
# - Profile Router ('api/profile/$')
# profileRouter = routers.DefaultRouter()
# profileRouter.register(r'favorite-actors', profile.FavoriteActorViewSet)
# profileRouter.register(r'favorite-genres', profile.FavoriteGenreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(rootRouter.urls)),
    # path('profiles/<int:pk>/', include(profileRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
