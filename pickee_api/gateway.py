import requests
from django.http import JsonResponse

from pickee_api.models import Actor, Movie, MovieCast, FavoriteGenre, FavoriteActor, FavoriteMovie, MovieKeyword
from pickee_api.utils import BearerAuth, FavoriteFilter
from django.views.decorators.csrf import csrf_exempt

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


# GET request

# {
#     "results": [
#         {
#             "logo": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAGB.png?w=92&auto=compress&app_version=a0041586-5e2a-4a1d-8e92-e9d1d3a9feaf_erss2020-01-13",
#             "name": "Netflix",
#             "url": "https://www.netflix.com/title/70298933"
#         },
#         {
#             "logo": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAGB.png?w=92&auto=compress&app_version=a0041586-5e2a-4a1d-8e92-e9d1d3a9feaf_erss2020-01-13",
#             "name": "Netflix",
#             "url": "https://www.netflix.com/title/70298933"
#         }
#     ]
# }
def get_streaming_service(request):
    if request.method == 'POST':
        url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
        headers = {"x-rapidapi-key": UTELLY_API_KEY}
        params = {"term": request.POST['movie_name'], "country": "uk"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return JsonResponse(data)


# GET REQUEST
# RESPONSE
# {
#     "id": 287,
#     "name": "Brad Pitt",
#     "picture": "https://image.tmdb.org/t/p/w500/pCUdYAaarKqY2AAUtV6xXYO8UGY.jpg"
# }
def search_actors(request):
    if request.method == 'POST':
        actor_name = request.POST['actor_name']
        actor_name.replace(' ', '+')
        url = 'https://api.themoviedb.org/3/search/person?query=' + actor_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        actor_options = data['results']

        # TODO: create actor object in database depending on user selection

        return JsonResponse(actor_options)


def search_movies(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        movie_name.replace(' ', '+')
        url = 'https://api.themoviedb.org/3/search/movie?query=' + movie_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()

        # TODO: create movie object in database depending on user selection

        return JsonResponse(data)


# def get_cast(request):
#     if request.method == 'POST':
#         movie_id = request.POST['movie_id']
#         url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/credits?'
#
#         response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
#         data = response.json()
#         cast = data['cast']
#
#         movie = Movie.objects.get(id=movie_id)  # assumes movie is already in database
#         for index in range(4):
#             actor_data = cast[index]
#             Actor.objects.get_or_create(id=actor_data['id'], name=actor_data['name'])
#             actor = Actor.objects.get(id=actor_data['id'])
#             movie_cast = MovieCast.objects.get_or_create(movie=movie, actor=actor)
#
#         return JsonResponse(data)

def get_cast(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/credits?'

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        cast = data['cast']

        movie = Movie.objects.get(id=movie_id)  # assumes movie is already in database
        for index in range(4):
            actor_data = cast[index]
            Actor.objects.get_or_create(id=actor_data['id'], name=actor_data['name'])
            actor = Actor.objects.get(id=actor_data['id'])
            movie_cast = MovieCast.objects.get_or_create(movie=movie, actor=actor)

        return JsonResponse(data)


# Create a recommendation
# Payload example
# REQUEST
# {
#     "runtime": 30,
#     "genres": "Horror, Comedy",
#     "users": [82, 59]
# }

# /api/recommendation
@csrf_exempt
def get_recommendation(request):
    """
            Performs the Pickee recommendation algorithm with the given input
             then creates and returns a recommendation.
    """
    print(request.POST)
    # print(request.user.is_authenticated)
    if request.method == 'POST':
        # Takes into consideration the casual preferences of the movie session
        # RUNTIME | GENRES | ASSOCIATED USERS
        runtime = request.POST['runtime']
        casual_genres = request.POST['genres']
        users = request.POST.getlist('users')
        users.append(request.user.id)

        # Retrieves the favorite genres shared between all users of the session
        common_favorite_genres = FavoriteFilter(model=FavoriteGenre).get_common(users=users)
        # Combines the genres selected as casual preferences with the ones marked as "favorites"
        combined_genres = list(set(casual_genres.genre.id) | set(common_favorite_genres.genre.id))
        # Joins the combined genres separating the values with a comma
        genre_string = ','.join(combined_genres)

        # Retrieves the favorite actors shared between all users of the session
        common_favorite_actors = FavoriteFilter(model=FavoriteActor).get_common(users=users)
        # Joins the common actors with a pipe character to indicate "OR" logic
        actor_string = '|'.join(common_favorite_actors.actor.id)

        # Retrieves the favorite movies shared between all users of the session
        common_favorite_movies = FavoriteFilter(model=FavoriteMovie).get_common(users=users)

        # Retrieves the keywords associated with the common movies
        keywords = get_movie_keywords(common_favorite_movies)
        keyword_string = '|'.join(keywords)

        # Builds the request URL
        query_params = {
            'language': 'en-UK',
            'sort_by': 'popularity.desc',
            'with_genres': genre_string,
            'with_actors': actor_string,
            'with_runtime.lte': runtime,
            'with_keywords': keyword_string,
        }

        url = 'https://api.themoviedb.org/3/discover/movie'

        # Executes the GET request in The Movie Database API service (/discover/movie)
        response = requests.get(url, params=query_params, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()
        recommendation = data['results'][0]

        # Retrieves the cast data
        # TODO: Finish cast endpoint

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


def get_movie_keywords(movies):
    keywords = set()
    for movie in movies:
        movie_keywords = MovieKeyword.objects.filter(movie=movie)
        for keyword in movie_keywords:
            keywords.add(keyword)
    return keywords
