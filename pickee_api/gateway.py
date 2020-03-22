import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from pickee_api.models import Movie, FavoriteGenre, FavoriteActor, FavoriteMovie, MovieKeyword, \
    PickeeUser, Recommendation
from pickee_api.utils import BearerAuth, FavoriteFilter

# The token was kept here to simplify the marking process
# In a real-world scenario we would never commit this token
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NjZjYTNlNDMxOWE4MzVjYWVlODI2MmE3YTgzZjNiNCIsInN1YiI6IjVlNjUwMDM3MTUxYzVjMDAxNWZmYWYyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iLqC8qnysp7u5Ha5ChC1Ag8iiLQP9zyWikURmHH7L48"
UTELLY_API_KEY = "ed03a46877msh52c7837560678fep10a146jsnaac521c60402"

TMDB_ITEMS_PER_PAGE = 20


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
    if request.method == 'GET':
        # Retrieve actor name query param
        actor_name = request.GET.get('name')
        # Build query params to hit TMDB API
        query_parms = {
            'query': actor_name
        }
        # Set the TMDB endpoint
        url = 'https://api.themoviedb.org/3/search/person'
        # Perform the GET request
        personResponse = requests.get(url, params=query_parms, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        # Parse the request payload into JSON
        personData = personResponse.json()
        # Prepare response payload
        response = {}
        if personData.get('results'):
            results = personData['results']
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

        elif personResponse.text:
            # Forwards TMDB API error
            response = personData

        return JsonResponse(response)


def search_movies(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        movie_name.replace(' ', '+')
        url = 'https://api.themoviedb.org/3/search/movie?query=' + movie_name

        response = requests.get(url, auth=BearerAuth(TMDB_ACCESS_TOKEN))
        data = response.json()

        # TODO: create movie object in database depending on user selection

        return JsonResponse(data)


# Create a recommendation
# REQUEST BODY
# {
#     "runtime": 30,
#     "genre_ids": "1,2",
#     "user_ids": [82, 59],
#     "session_id" 12,
#     "offset": 0,
# }
# /api/recommendation
def generate_recommendation(request):
    """
            Performs the Pickee recommendation algorithm with the given input
             then creates and returns a recommendation.
    """
    print(request.POST)
    # print(request.user.is_authenticated)
    if request.method == 'POST':
        # Takes into consideration the casual preferences of the movie session
        # RUNTIME | GENRES | ASSOCIATED USERS
        runtime = request.POST.get('runtime')
        casual_genre_ids = request.POST.get('genre_ids')
        user_ids = request.POST.getlist('user_ids')
        session_id = request.POST.get('session_id')
        offset = int(request.POST['offset'])

        # If authenticated, add the user id to users
        if request.user.is_authenticated:
            user_ids.append(request.user.id)

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
            response = __get_response_payload(discoverData, index, offset)

            # Retrieves the cast data
            response['cast'] = __get_movie_cast(response.get('id'))

            # Adds the movie and recommendation to the database
            __create_objects(response, session_id)
        elif discoverResponse.text:
            # Forwards TMDB API error
            response = discoverData

        return JsonResponse(response)


def __get_response_payload(discover_data, index, offset):
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


def __create_objects(response, session_id):
    movie = Movie.objects.get_or_create(id=response['id'],
                                        name=response['name'],
                                        image_url=response['image_url'],
                                        rating=response['rating'],
                                        release_date=response['release_date'],
                                        description=response['description'])
    rec = Recommendation(movie=movie[0], session_id=session_id)
    rec.save()
