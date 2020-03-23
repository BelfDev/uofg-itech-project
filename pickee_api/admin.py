from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from pickee_api import models
from pickee_api.forms import PickeeUserCreationForm, PickeeUserChangeForm
from pickee_api.models import PickeeUser


# Custom admin for the PickeeUser
@admin.register(models.PickeeUser)
class CustomUserAdmin(UserAdmin):
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
    list_display = ['user', 'genre']


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
admin.site.register(models.Genre)
admin.site.register(models.Keyword)
admin.site.register(models.MovieKeyword)
