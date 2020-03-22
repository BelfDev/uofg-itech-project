import collections
from typing import TypeVar, Generic

import requests
from django.db.models import Count

from pickee_api.models import FavoriteGenre, FavoriteActor, FavoriteMovie, PickeeUser

FavoriteModel = TypeVar('FavoriteModel', FavoriteGenre, FavoriteActor, FavoriteMovie)


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class FavoriteFilter(Generic[FavoriteModel]):
    def __init__(self, model):
        self.model = model
        self.value = {
            FavoriteGenre: 'genre',
            FavoriteMovie: 'movie',
            FavoriteActor: 'actor',
        }[model]

    def get_common(self, users: [PickeeUser]):
        """
        Returns the common favorite models shared by the given users.

        Example: if passed in the FavoriteGenre model it will return all the common favorite genres
        """
        all_favorites = self.model.objects.filter(user__in=users).values_list(self.value, flat=True)
        common_favorites = [item for item, count in collections.Counter(all_favorites).items() if count > 1]
        return common_favorites
