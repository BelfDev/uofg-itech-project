import requests
from django.http import JsonResponse

from pickee_api.utils import BearerAuth
from pickee_api.models import Actor,Movie,MovieCast,FavoriteGenre

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
    if request.method == 'POST':
        actor_name = request.POST['actor_name']
        actor_name.replace(' ','+')
        url = 'https://api.themoviedb.org/3/search/person?query='+actor_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        actor_options = data['results']

        #TODO: create actor object in database depending on user selection

        return JsonResponse(actor_options)

def search_movies(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        movie_name.replace(' ','+')
        url = 'https://api.themoviedb.org/3/search/movie?query='+movie_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()

        #TODO: create movie object in database depending on user selection

        return JsonResponse(data)

def get_cast(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        url ='https://api.themoviedb.org/3/movie/'+movie_id+'/credits?'

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        cast = data['cast']

        movie = Movie.objects.get(id=movie_id) #assumes movie is already in database
        for index in range(4):
            actor_data = cast[index]
            Actor.objects.get_or_create(id=actor_data['id'],name=actor_data['name'])
            actor = Actor.objects.get(id=actor_data['id'])
            movie_cast = MovieCast.objects.get_or_create(movie=movie,actor=actor)

        return JsonResponse(data)

def get_recommendation(request):
    if request.method == 'POST':
        genres = request.POST['casual_genres']
        runtime = request.POST['runtime']
        users = request.POST['users']
        actors = '31|6193|74568|4491'
        #keywords
        #certification
        url ='''https://api.themoviedb.org/3/discover/movie?language=en-UK&sort_by=popularity.desc&page=1
                &with_genres='''+genres+'&with_actors='+actors+'&with_runtime.lte='+runtime

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        recommendation = data['results'][0]
        recommendation_dict = {
            'id': recommendation['id'],
            'name': recommendation['title'],
            'image_url': recommendation['poster_path'],
            'rating': recommendation['vote_average'],
            'release_date': recommendation['release_date'],
            'description': recommendation['overview'],
            'cast': []
        }

        return JsonResponse(recommendation_dict)

def get_common_favorite_genres(users):
    all_favorite_genres = []
    common_favorite_genres = []

    for user in users:
        favorite_genres = get_favorite_genres(user)
        for genre in favorite_genres:
            if genre in all_favorite_genres:
                common_favorite_genres.append(genre)
            else:
                all_favorite_genres.append(genre)    
    
    return common_favorite_genres

def get_favorite_genres(user):
    favorite_genres = FavoriteGenre.objects.get(user=user)
    genres = []
    for genre in favorite_genres:
        genres.append(genre)
    
    return genres