from django.test import TestCase
from pickee_api.models import Movie

class MovieModelTest(TestCase):
    def test_ensure_rating_is_positive(self):
        movie = Movie.objects.create(id=1,name='Test Movie',rating=5)
        movie.save()

        self.assertEquals((movie.rating >= 0), True)