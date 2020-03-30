from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from pickee_api import models
from pickee_api.forms import PickeeUserCreationForm, PickeeUserChangeForm
from pickee_api.models import PickeeUser


# This file contains all admin panel custom configurations

@admin.register(models.PickeeUser)
class CustomUserAdmin(UserAdmin):
    """
        A custom admin panel visualization for the PickeeUser model
    """
    add_form = PickeeUserCreationForm
    form = PickeeUserChangeForm
    model = PickeeUser
    list_display = ('id', 'email', 'first_name')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'first_name', 'last_name', 'picture', 'gender', 'age', 'associated_users')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff', 'is_active', 'first_name', 'last_name', 'picture',
                'gender', 'age', 'associated_users')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(models.FavoriteGenre)
class FavoriteGenreAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['user', 'genre']


@admin.register(models.FavoriteActor)
class FavoriteActorAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['user', 'actor']


@admin.register(models.FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['user', 'movie']


@admin.register(models.MovieCast)
class MovieCastAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['movie', 'actor']


@admin.register(models.MovieKeyword)
class MovieKeywordAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['movie', 'keyword']


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['id']


@admin.register(models.Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    # Changes the displayed attributes on the admin list
    list_display = ['id', 'movie', 'user_choice']


# Registers the remaining Pickee API models in the admin site
admin.site.register(models.Actor)
admin.site.register(models.Movie)
admin.site.register(models.Genre)
admin.site.register(models.Keyword)
