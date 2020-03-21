import json

import requests
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from pickee_api.models import PickeeUser

# Temporary renders login.html
from pickee_api.forms import PickeeUserCreationForm

def home(request):
    data = json.dumps({
        "user": get_user_data(request),
    });
    context = {'data': data}
    return render(request, 'home.html', context=context)

def recommendation(request):
    data = json.dumps({
        "user": get_user_data(request),
        # TODO: pass real data
        "recommendation": {
            "id": 1,
            "name": "The Green Mile",
            "image_url": "/sOHqdY1RnSn6kcfAHKu28jvTebE.jpg",
            "rating": "8.5",
            "release_date": "1999-12-10",
            "description": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
            "cast": [
                {
                    "id": 31,
                    "name": "Tom Hanks",
                },
                {
                    "cast_id": 5,
                    "name": "Michael Clarke Duncan",
                }
            ]
        }
    })
    context = {'data': data}

    return render(request, 'recommendation.html', context=context)

def user_login(request):
    if request.method == 'POST':
        # Retrieves username and password
        email = request.POST['email']
        password = request.POST['password']
        # Authenticates the user
        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:
                # If valid, log in the user
                login(request, user)
                return redirect('home')
        else:
            # If there are any authentication errors, send error feedback
            loginFeedback = json.dumps({
                "error": "invalid credentials"
            })
            context = {'loginFeedback': loginFeedback}
            return render(request, 'login.html', context=context)
    else:
        return render(request, 'login.html')


# Temporary renders signup.html
def user_signup(request):
    if request.method == 'POST':
        form = PickeeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = authenticate(email=email, password1=password1, password2=password2)
            login(request, user)
            return redirect('home')
        else:
            errorMsgs = {}
            for field in form:
                errorMsgs[str(field.label)] = field.errors

            signupFeedback = json.dumps({
                'errors': errorMsgs
            })
            context = {'signupFeedback': signupFeedback}
            return render(request, 'signup.html', context=context)
    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def profile_main(request):
    user_profile_data = { "age": request.user.age, "gender": request.user.gender }
    data = json.dumps({
        "user": {**get_user_data(request), **user_profile_data}
    });
    context = {'data': data}
    return render(request, 'profile_main.html', context=context)

def profile_preferences(request):
    data = json.dumps({
        "user": get_user_data(request),
    });
    context = {'data': data}
    return render(request, 'profile_preferences.html', context=context)

def profile_history(request):
    data = json.dumps({
        "user": get_user_data(request),
    });
    context = {'data': data}
    return render(request, 'profile_history.html', context=context)


# Helper methods

def get_user_data(request):
    if not request.user.is_authenticated:
        return {}

    return {
        "id": request.user.id,
        "name": request.user.first_name,
        "email": request.user.email,
        "picture": request.user.picture.url if request.user.picture else None
    }

    