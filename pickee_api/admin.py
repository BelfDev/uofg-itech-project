from django.contrib import admin

from pickee_api import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name']
    list_editable = ['email', 'first_name']
    ordering = ['id']


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(models.Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user_choice']


# Registers Pickee API models in the admin site
admin.site.register(models.FavoriteActor)
admin.site.register(models.Actor)
admin.site.register(models.FavoriteMovie)
admin.site.register(models.Movie)
admin.site.register(models.MovieCast)
admin.site.register(models.FavoriteGenre)
admin.site.register(models.Genre)
