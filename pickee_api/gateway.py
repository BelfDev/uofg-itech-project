import requests
from django.http import JsonResponse

from pickee_api.utils import BearerAuth
from pickee_api.models import Actor

# The token was kept here to simplify the marking process
# In a real-world scenario we would never commit this token
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NjZjYTNlNDMxOWE4MzVjYWVlODI2MmE3YTgzZjNiNCIsInN1YiI6IjVlNjUwMDM3MTUxYzVjMDAxNWZmYWYyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iLqC8qnysp7u5Ha5ChC1Ag8iiLQP9zyWikURmHH7L48"
UTELLY_API_KEY = "ed03a46877msh52c7837560678fep10a146jsnaac521c60402"


def tmdb_example_endpoint(request):
    if request.method == 'GET':
        url = 'https://api.themoviedb.org/3/movie/popular'
        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        return JsonResponse(data)


def utelly_example_endpoint(request):
    if request.method == 'GET':
        url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
        headers = {"x-rapidapi-key": UTELLY_API_KEY}
        params = {"term": "bojack", "country": "uk"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return JsonResponse(data)

def search_actors(request):
    if request.method == 'GET':
        actor_name = 'James Corden'
        actor_name.replace(' ','+')
        url = 'https://api.themoviedb.org/3/search/person?query='+actor_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        # top_result = data['results'][0]
        # actor = Actor.objects.get_or_create(id=top_result['id'],name=top_result['name'])

        return JsonResponse(data)

def search_movies(request):
    if request.method == 'GET':
        movie_name = 'Trolls'
        movie_name.replace(' ','+')
        url = 'https://api.themoviedb.org/3/search/movie?query='+movie_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()

        #TODO: create movie object in database depending on user selection

        return JsonResponse(data)
