from django.test import TestCase
from pickee_api.models import Movie, PickeeUser, Genre, FavoriteGenre
from pickee_api.utils import FavoriteFilter
import datetime

class MovieModelTest(TestCase):
    def test_ensure_rating_is_positive(self):
        movie = Movie.objects.create(id=1,name='Test Movie',rating=5)
        self.assertTrue(movie.rating >= 0)
    
    def test_ensure_rating_is_less_than_or_equal_to_ten(self):
        movie = Movie.objects.create(id=2,name='Test Movie',rating=6)
        self.assertTrue(movie.rating <= 10)
    
    def test_release_date_in_past(self):
        movie = Movie.objects.create(id=3,name='Test Movie',rating=7,release_date=datetime.date(2019,11,12))
        self.assertTrue(movie.release_date < datetime.date.today())

class RecommendationAlgorithmTest(TestCase):
    def test_retrieve_common_favorite_genres(self):
        user1 = PickeeUser.objects.create_user('user1@email.com','user1password')
        user2 = PickeeUser.objects.create_user('user2@email.com','user2password')
        users = [user1,user2]

        action = Genre.objects.create(id=1,name='action')
        adventure = Genre.objects.create(id=2,name='adventure')
        animation = Genre.objects.create(id=3,name='animation')

        FavoriteGenre.objects.create(user=user1,genre=action)
        FavoriteGenre.objects.create(user=user1,genre=adventure)
        FavoriteGenre.objects.create(user=user2,genre=action)
        FavoriteGenre.objects.create(user=user2,genre=animation)

        favorite_genre_filter = FavoriteFilter(FavoriteGenre)
        common_favorite_genre = favorite_genre_filter.get_common(users)
        common_favorite_genre_object = Genre.objects.get(id=common_favorite_genre[0])
        
        self.assertEqual(len(common_favorite_genre),1)
        self.assertEqual(common_favorite_genre_object.name,'action')