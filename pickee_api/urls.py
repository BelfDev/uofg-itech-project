from django.urls import include, path
from rest_framework import routers

from pickee_api.views import auth, profile, recommendation

app_name = 'pickee_api'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', auth.UserViewSet)

router.register(r'profile', profile.UserProfileViewSet)
router.register(r'profile/favorite-actor', profile.FavoriteActorViewSet)
router.register(r'profile/actor', profile.ActorViewSet)
router.register(r'profile/favorite-movie', profile.FavoriteMovieViewSet)
router.register(r'profile/movie', profile.MovieViewSet)
router.register(r'profile/movie-cast', profile.MovieCastViewSet)
router.register(r'profile/movie', profile.MovieViewSet)
router.register(r'profile/favorite-genre', profile.FavoriteGenreViewSet)
router.register(r'profile/genre', profile.GenreViewSet)

router.register(r'recommendation', recommendation.RecommendationViewSet)
router.register(r'recommendation/session', recommendation.SessionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
