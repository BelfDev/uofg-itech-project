import json

import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from pickee_api.models import Movie, FavoriteGenre, FavoriteActor, FavoriteMovie, MovieKeyword, \
    PickeeUser, Recommendation
from pickee_api.utils import BearerAuth, FavoriteFilter

# The token was kept here to simplify the marking process
# In a real-world scenario we would never commit this token
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NjZjYTNlNDMxOWE4MzVjYWVlODI2MmE3YTgzZjNiNCIsInN1YiI6IjVlNjUwMDM3MTUxYzVjMDAxNWZmYWYyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iLqC8qnysp7u5Ha5ChC1Ag8iiLQP9zyWikURmHH7L48"
UTELLY_API_KEY = "ed03a46877msh52c7837560678fep10a146jsnaac521c60402"

TMDB_ITEMS_PER_PAGE = 20


def get_available_providers(request):
    """
        Searches for available content providers via Utelly API service
    """
    if request.method == 'GET':
        # Retrieves the movie_name query parameter
        movie_name = request.GET.get('movie_name')
        # Sets utelly endpoint
        url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
        # Sets the necessary headers
        headers = {"x-rapidapi-key": UTELLY_API_KEY}
        # Sets the query parameters
        query_params = {"term": movie_name,
                        "country": "uk"}
        # Hits utelly API and gets the available streaming providers
        utellyResponse = requests.get(url, headers=headers, params=query_params)
        # Parses the response into JSON
        data = utellyResponse.json()

        response = {}
        if data.get('results'):
            relevant_result = data.get('results')[0]
            locations = relevant_result.get('locations')
            providers = []
            if locations:
                for location in locations:
                    provider = {
                        'logo': location.get('icon'),
                        'name': location.get('display_name'),
                        'url': location.get('url')
                    }
                    providers.append(provider)
            response['results'] = providers
            response['movie_name'] = relevant_result.get('name')
            response['term'] = data.get('term')

        return JsonResponse(response)

@login_required
def search_actors(request):
    """
        Searches for actors via The Movie DB /search/movie resource
    """
    if request.method == 'GET':
        # Retrieve actor name query param
        actor_name = request.GET.get('name')
        # Set the TMDB endpoint
        url = 'https://api.themoviedb.org/3/search/person'
        # Search for actors with the given name with TMDB API
        searchData = __search_by_name(url, actor_name)
        # Prepare response payload
        response = {}
        if searchData.get('results'):
            results = searchData['results']
            actors = []
            # Formats the results payload
            for result in results:
                actor = {
                    'id': result['id'],
                    'name': result['name']
                }

                profile_path = result['profile_path']
                actor['image_url'] = None if not profile_path else 'https://image.tmdb.org/t/p/w500' + profile_path
                actors.append(actor)

            response['results'] = actors

        elif searchData.get('errors'):
            # Forwards TMDB API error
            response = searchData

        return JsonResponse(response)


@login_required
def search_movies(request):
    """
        Searches for movies via The Movie DB /search/movie resource
    """
    if request.method == 'GET':
        # Retrieve movie name query param
        movie_name = request.GET.get('name')
        # Set the TMDB endpoint
        url = 'https://api.themoviedb.org/3/search/movie'
        # Perform the GET request
        searchData = __search_by_name(url, movie_name)
        # Prepare response payload
        response = {}
        if searchData.get('results'):
            results = searchData['results']
            movies = []
            # Formats the results payload
            for result in results:
                movie = {
                    'id': result.get('id'),
                    'name': result.get('title'),
                    'rating': result.get('vote_average'),
                    'release_date': result.get('release_date'),
                    'description': result.get('overview')
                }
                # Adds the image_url
                poster_path = result['poster_path']
                movie['image_url'] = None if not poster_path else 'https://image.tmdb.org/t/p/w500' + poster_path
                # Adds the movie cast
                movie['cast'] = __get_movie_cast(movie['id'])

                movies.append(movie)

            response['results'] = movies

        elif searchData.get('errors'):
            # Forwards TMDB API error
            response = searchData

        return JsonResponse(response)


def generate_recommendation(request):
    """
        Performs the Pickee recommendation algorithm with the given input
        then creates and returns a recommendation.
    """
    print(request.POST)
    # print(request.user.is_authenticated)
    if request.method == 'POST':
        # Parses AJAX POST body
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Takes into consideration the casual preferences of the movie session
        # RUNTIME | GENRES | ASSOCIATED USERS
        runtime = body.get('runtime')
        casual_genre_ids = body.get('genre_ids')
        user_ids = body.get('user_ids')
        session_id = body.get('session_id')
        offset = int(body['offset'])

        # If authenticated, add the user id to users
        if request.user.is_authenticated:
            user_ids.append(request.user.id)

        # Initializes genre_string
        genre_string = casual_genre_ids
        # Initializes actor_string
        actor_string = None
        # Initializes keyword_string
        keyword_string = None

        if user_ids:
            # Converts the user ids to a list of PickeeUser
            users = PickeeUser.objects.filter(id__in=user_ids)

            # Retrieves the favorite genres shared between all users of the session
            common_favorite_genres = FavoriteFilter(model=FavoriteGenre).get_common(users=users)

            # Combines the genres selected as casual preferences with the ones marked as "favorites"
            combined_genre_ids = __get_combined_genre_ids(casual_genre_ids, common_favorite_genres)
            # Joins the combined genres separating the values with a comma
            genre_string = ','.join(combined_genre_ids)

            # Retrieves the favorite actors shared between all users of the session
            common_favorite_actors = FavoriteFilter(model=FavoriteActor).get_common(users=users)
            # Joins the common actors with a pipe character to indicate "OR" logic
            actor_string = '|'.join(list(map(str, common_favorite_actors)))

            # Retrieves the favorite movies shared between all users of the session
            common_favorite_movies = FavoriteFilter(model=FavoriteMovie).get_common(users=users)

            # Retrieves the keywords associated with the common movies
            keywords = __get_movie_keywords(common_favorite_movies)
            keyword_string = '|'.join(list(map(str, keywords)))

        # Infers the TMDB page based on the offset
        page = (offset // TMDB_ITEMS_PER_PAGE) + 1

        # Builds the request URL
        query_params = {
            'language': 'en-UK',
            'sort_by': 'popularity.desc',
            'page': page,
            'with_genres': genre_string,
            'with_cast': actor_string,
            'with_runtime.lte': runtime,
            'with_keywords': keyword_string,
        }

        url = 'https://api.themoviedb.org/3/discover/movie'

        # Executes the GET request in The Movie Database API service (/discover/movie)
        discoverResponse = requests.get(url, params=query_params, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        discoverData = discoverResponse.json()

        # Evaluates which index should be accessed in the results array
        index = offset if offset < TMDB_ITEMS_PER_PAGE else TMDB_ITEMS_PER_PAGE - offset

        # Prepares response payload
        response = {}
        if discoverData.get('results'):
            response = __get_recommendation_response_payload(discoverData, index, offset)

            # Retrieves the cast data
            response['cast'] = __get_movie_cast(response.get('id'))

            if session_id:
                # Creates the recommendation object if TMDB returned results and if the user has passed a session id
                recommendation = __create_recommendation_objects(response, session_id)
                response['recommendation_id'] = recommendation.id
        elif discoverResponse.text:
            # Forwards TMDB API error
            response = discoverData

        return JsonResponse(response)


def __search_by_name(url, name):
    # Build query params to hit TMDB API
    query_parms = {
        'query': name
    }
    # Perform the GET request
    response = requests.get(url, params=query_parms, auth=BearerAuth(TMDB_ACCESS_TOKEN))
    # Parse the request payload into JSON
    return response.json()


def __get_recommendation_response_payload(discover_data, index, offset):
    recommendation = discover_data['results'][index]
    response = {
        'id': recommendation.get('id'),
        'name': recommendation.get('title'),
        'rating': recommendation.get('vote_average'),
        'release_date': recommendation.get('release_date'),
        'description': recommendation.get('overview'),
        'cast': [],
        'last_offset': offset
    }

    image_path = recommendation.get('poster_path')
    response['image_url'] = None if not image_path else 'https://image.tmdb.org/t/p/w500' + image_path
    return response


def __get_movie_keywords(movies):
    return MovieKeyword.objects.filter(movie__in=movies).values_list('keyword', flat=True)


def __get_combined_genre_ids(casual_genres_string, favorite_genres):
    # Converts the casual genres string into an array of genre ids
    casual_genre_ids = [s.strip() for s in casual_genres_string.split(',')]
    # Creates a set of combined genres (excluding duplicates)
    combined_genres = set(casual_genre_ids + list(map(str, favorite_genres)))
    return combined_genres


def __get_movie_cast(movie_id):
    castUrl = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
    castResponse = requests.get(castUrl, auth=BearerAuth(TMDB_ACCESS_TOKEN))
    castData = castResponse.json()
    return castData.get('cast')[:5]


def __create_recommendation_objects(response, session_id):
    movie = Movie.objects.get_or_create(id=response['id'],
                                        name=response['name'],
                                        image_url=response['image_url'],
                                        rating=response['rating'],
                                        release_date=response['release_date'],
                                        description=response['description'])
    rec = Recommendation(movie=movie[0], session_id=session_id)
    rec.save()
    return rec
