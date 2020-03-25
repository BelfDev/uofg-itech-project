from django.test import TestCase
from pickee_api.models import Movie
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