import requests
from django.http import JsonResponse

from pickee_api.utils import BearerAuth

# The token was kept here to simplify the marking process
# In a real-world scenario we would never commit this token
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NjZjYTNlNDMxOWE4MzVjYWVlODI2MmE3YTgzZjNiNCIsInN1YiI6IjVlNjUwMDM3MTUxYzVjMDAxNWZmYWYyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iLqC8qnysp7u5Ha5ChC1Ag8iiLQP9zyWikURmHH7L48"


def tmdb_example_endpoint(request):
    if request.method == 'GET':
        url = 'https://api.themoviedb.org/3/movie/popular'
        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        return JsonResponse(data)


def utelly_example_endpoint(request):
    if request.method == 'GET':
        url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
        headers = {"x-rapidapi-key": "ed03a46877msh52c7837560678fep10a146jsnaac521c60402"}
        params = {"term": "bojack", "country": "uk"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return JsonResponse(data)
