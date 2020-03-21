from typing import TypeVar, Generic

import requests

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

    def get_common(self, users: [PickeeUser]):
        """
        Returns the common favorite models shared by the given users.

        Example: if passed in the FavoriteGenre model it will return all the common favorite genres
        """
        all_favorites = []
        common_favorites = []

        for user in users:
            favorites = self.model.objects.filter(user=user)
            for favorite in favorites:
                if favorite in all_favorites:
                    common_favorites.append(favorite)
                else:
                    all_favorites.append(favorite)

        return common_favorites
