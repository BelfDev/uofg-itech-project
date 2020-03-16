from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import PickeeUser


class PickeeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = PickeeUser
        fields = ('email',)


class PickeeUserChangeForm(UserChangeForm):
    class Meta:
        model = PickeeUser
        fields = ('email',)
