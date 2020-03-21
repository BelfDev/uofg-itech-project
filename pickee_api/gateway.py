import requests
from django.http import JsonResponse

from pickee_api.models import Actor, Movie, MovieCast, FavoriteGenre, FavoriteActor, FavoriteMovie, MovieKeyword
from pickee_api.utils import BearerAuth

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


def get_streaming_service(request):
    if request.method == 'POST':
        url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
        headers = {"x-rapidapi-key": UTELLY_API_KEY}
        params = {"term": request.POST['movie_name'], "country": "uk"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return JsonResponse(data)


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
# {
#     "time": "30",
#     "genres": ["Horror, Comedy"],
#     "users": [82, 59]
# }
def get_recommendation(request):
    if request.method == 'POST':
        users = request.POST['users']
        runtime = request.POST['runtime']

        casual_genres = request.POST['casual_genres']
        common_favorite_genres = get_common_favorites(users, FavoriteGenre)
        combined_genres = list(set(casual_genres.genre.id) | set(common_favorite_genres.genre.id))
        genre_string = ','.join(combined_genres)

        common_favorite_actors = get_common_favorites(users, FavoriteActor)
        actor_string = '|'.join(common_favorite_actors.actor.id)

        common_favorite_movies = get_common_favorites(users, FavoriteMovie)
        keywords = get_movie_keywords(common_favorite_movies)
        keyword_string = '|'.join(keywords)

        # certification
        url = '''https://api.themoviedb.org/3/discover/movie?language=en-UK&sort_by=popularity.desc&page=1
                &with_genres=''' + genre_string + '&with_actors=' + actor_string + '''&with_runtime.lte=
                ''' + runtime + '&with_keywords=' + keyword_string

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


def get_common_favorites(users, model):
    all_favorites = []
    common_favorites = []

    for user in users:
        favorites = model.objects.filter(user=user)
        for favorite in favorites:
            if favorite in all_favorites:
                common_favorites.append(favorite)
            else:
                all_favorites.append(favorite)

    return common_favorites


def get_movie_keywords(movies):
    keywords = {}
    for movie in movies:
        movie_keywords = MovieKeyword.objects.filter(movie=movie)
        for keyword in movie_keywords:
            keywords.add(keyword.id)
    return keywords
