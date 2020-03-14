import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickee_project.settings')
import django
django.setup()
from pickee_api.models import (UserProfile,FavoriteActor,Actor,
                                FavoriteMovie,Movie,MovieCast,
                                FavoriteGenre,Genre,Recommendation,
                                Session)

users = [
    {}
]

favorite_actors = [
    {}
]

actors = [
    {}
]

favorite_movies = [
    {}
]

movies = [
    {}
]

movie_casts = [
    {}
]

favorite_genres = [
    {}
]

genres = [
    {}
]

recommendations = [
    {}
]

sessions = [
    {}
]