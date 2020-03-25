from django.test import TestCase
from pickee_api.models import Movie

class MovieModelTest(TestCase):
    def test_ensure_rating_is_positive(self):
        movie = Movie.objects.create(id=1,name='Test Movie',rating=5)
        self.assertEquals((movie.rating >= 0), True)
    
    def test_ensure_rating_is_less_than_or_equal_to_ten(self):
        movie = Movie.objects.create(id=2,name='Test Movie',rating=6)
        self.assertEquals((movie.rating <= 10), True)