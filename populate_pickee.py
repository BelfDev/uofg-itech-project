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
    {'person_id':31,'name':'Tom Hanks','picture':'null'},
    {'person_id':6193,'name':'Leonardo DiCaprio','picture':'null'},
    {'person_id':74568,'name':'Chris Hemsworth','picture':'null'},
    {'person_id':4491,'name':'Jennifer Aniston','picture':'null'},
    {'person_id':11701,'name':'Angelina Jolie','picture':'null'},
    {'person_id':84223,'name':'Anna Kendrick','picture':'null'},
    {'person_id':192,'name':'Morgan Freeman','picture':'null'}
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