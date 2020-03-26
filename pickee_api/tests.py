from django.test import TestCase
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from pickee_api.models import Movie,PickeeUser,Genre,FavoriteGenre,FavoriteMovie, \
                                Actor,FavoriteActor,Session,Recommendation
from pickee_api.utils import FavoriteFilter
import datetime

class PickeeUserTest(TestCase):
    def test_ensure_email_format_correct(self):
        user = PickeeUser.objects.create_user('user@email.com','userpassword')
        try:
            validate_email(user.email)
            valid_email = True
        except ValidationError:
            valid_email = False
        self.assertTrue(valid_email)
    
    def test_ensure_age_is_positive(self):
        user = PickeeUser.objects.create_user('user@email.com','userpassword',age=20)
        self.assertTrue(user.age >= 0)
    
    def test_ensure_age_is_less_than_one_hundred(self):
        user = PickeeUser.objects.create_user('user@email.com','userpassword',age=40)
        self.assertTrue(user.age <= 100)
    
    def test_ensure_gender_is_valid(self):
        user = PickeeUser.objects.create_user('user@email.com','userpassword',gender='MALE')
        gender_choices = ['MALE','FEMALE','OTHER','UNSPECIFIED']
        self.assertIn(user.gender,gender_choices)

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

class RecommendationModelTest(TestCase):
    def test_ensure_user_choice_is_valid(self):
        user1 = PickeeUser.objects.create_user('user1@email.com','user1password')
        user2 = PickeeUser.objects.create_user('user2@email.com','user2password')

        session = Session.objects.create()
        session.users.add(user1)
        session.users.add(user2)

        movie = Movie.objects.create(id=1,name='Test Movie',rating=5)
        recommendation = Recommendation.objects.create(session=session,movie=movie,user_choice='ACCEPTED')
        user_choices = ['ACCEPTED','REJECTED','BOOKMARKED']

        self.assertIn(recommendation.user_choice,user_choices)

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
        common_favorite_genres = favorite_genre_filter.get_common(users)
        
        self.assertEqual(len(common_favorite_genres),1)
        self.assertEqual(common_favorite_genres,[1])
    
    def test_retrieve_common_favorite_movies(self):
        user1 = PickeeUser.objects.create_user('user1@email.com','user1password')
        user2 = PickeeUser.objects.create_user('user2@email.com','user2password')
        user3 = PickeeUser.objects.create_user('user3@email.com','user3password')
        users = [user1,user2,user3]

        movie1 = Movie.objects.create(id=1,name='movie1',rating=5)
        movie2 = Movie.objects.create(id=2,name='movie2',rating=3)
        movie3 = Movie.objects.create(id=3,name='movie3',rating=9)

        FavoriteMovie.objects.create(user=user1,movie=movie3)
        FavoriteMovie.objects.create(user=user2,movie=movie2)
        FavoriteMovie.objects.create(user=user3,movie=movie1)
        FavoriteMovie.objects.create(user=user3,movie=movie3)

        favorite_movie_filter = FavoriteFilter(FavoriteMovie)
        common_favorite_movies = favorite_movie_filter.get_common(users)
        
        self.assertEqual(len(common_favorite_movies),1)
        self.assertEqual(common_favorite_movies,[3])
    
    def test_retrieve_common_favorite_actors(self):
        user1 = PickeeUser.objects.create_user('user1@email.com','user1password')
        user2 = PickeeUser.objects.create_user('user2@email.com','user2password')
        user3 = PickeeUser.objects.create_user('user3@email.com','user3password')
        user4 = PickeeUser.objects.create_user('user4@email.com','user4password')
        users = [user1,user2,user3,user4]

        actor1 = Actor.objects.create(id=1,name='actor1')
        actor2 = Actor.objects.create(id=2,name='actor2')
        actor3 = Actor.objects.create(id=3,name='actor3')

        FavoriteActor.objects.create(user=user1,actor=actor1)
        FavoriteActor.objects.create(user=user1,actor=actor2)
        FavoriteActor.objects.create(user=user2,actor=actor1)
        FavoriteActor.objects.create(user=user2,actor=actor3)
        FavoriteActor.objects.create(user=user3,actor=actor1)
        FavoriteActor.objects.create(user=user3,actor=actor3)
        FavoriteActor.objects.create(user=user4,actor=actor1)

        favorite_actor_filter = FavoriteFilter(FavoriteActor)
        common_favorite_actors = favorite_actor_filter.get_common(users)
        
        self.assertEqual(len(common_favorite_actors),2)
        self.assertEqual(common_favorite_actors,[1,3])