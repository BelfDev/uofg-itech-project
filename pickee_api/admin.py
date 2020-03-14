from django.contrib import admin
from pickee_api import models

# Registers Pickee API models in the admin site
admin.site.register(models.UserProfile)
admin.site.register(models.FavoriteActor)
admin.site.register(models.Actor)
admin.site.register(models.FavoriteMovie)
admin.site.register(models.Movie)
admin.site.register(models.MovieCast)
admin.site.register(models.FavoriteGenre)
admin.site.register(models.Genre)
admin.site.register(models.Recommendation)
admin.site.register(models.Session)
