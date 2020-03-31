import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from pickee_api.forms import PickeeUserCreationForm
from pickee_api.models import Recommendation


# This file contains views that result in HTML content


def home(request):
    data = json.dumps({
        "user": __get_user_data(request)
    })
    urls = json.dumps(__get_urls());
    context = {'data': data, 'urls': urls}
    return render(request, 'home.html', context=context)


def about(request):
    urls = json.dumps(__get_urls());
    context = {'urls': urls}
    return render(request, 'about.html', context=context)


def recommendation(request):
    urls = json.dumps(__get_urls());
    user = json.dumps(__get_user_data(request))
    preferences = json.dumps(request.POST)
    context = {'user': user, 'preferences': preferences, 'urls': urls}

    return render(request, 'recommendation.html', context=context)


def user_login(request):
    urls = json.dumps(__get_urls())

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
                "error": "Invalid credentials"
            })
            urls = json.dumps(__get_urls());
            context = {'loginFeedback': loginFeedback, 'urls': urls}
            return render(request, 'login.html', context=context)
    else:
        context = {'urls': urls}
        return render(request, 'login.html', context=context)


def user_signup(request):
    urls = json.dumps(__get_urls())

    if request.method == 'POST':
        form = PickeeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            errorMsgs = {}
            for field in form:
                errorMsgs[str(field.label)] = field.errors

            signupFeedback = json.dumps({
                'errors': errorMsgs
            })
            context = {'signupFeedback': signupFeedback, 'urls': urls}
            return render(request, 'signup.html', context=context)
    context = {'urls': urls}
    return render(request, 'signup.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    urls = json.dumps(__get_urls());
    user_profile_data = {"age": request.user.age, "gender": request.user.gender}
    user = json.dumps({**__get_user_data(request), **user_profile_data})
    context = {'user': user, 'urls': urls}
    return render(request, 'profile.html', context=context)


@login_required
def history(request):
    urls = __get_urls();
    recommendations = __get_recommendation_history(request)
    results = []
    if recommendations:
        for recommendation in recommendations:
            movie = recommendation.movie
            result = {
                'id': recommendation.id,
                'user_choice': recommendation.user_choice,
                'session_id': recommendation.session_id,
                'movie': {
                    'id': movie.id,
                    'name': movie.name,
                    'image_url': movie.image_url
                },
            }
            results.append(result)

    data = json.dumps({
        "results": results,
        'urls': urls
    })
    context = {'data': data}
    return render(request, 'history.html', context=context)


@login_required
def preferences(request):
    urls = json.dumps(__get_urls());
    user = json.dumps(__get_user_data(request))
    context = {'user': user, 'urls': urls}
    return render(request, 'preferences.html', context=context)


# Helper methods

def __get_user_data(request):
    if not request.user.is_authenticated:
        return {}

    return {
        "id": request.user.id,
        "name": request.user.first_name + " " + request.user.last_name,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "picture": request.user.picture.url if request.user.picture else None
    }


def __get_urls():
    return {
        "home": reverse("home"),
        "about": reverse("about"),
        "login": reverse("login"),
        "logout": reverse("logout"),
        "signup": reverse("signup"),
        "profile": reverse("profile"),
        "preferences": reverse("preferences"),
        "history": reverse("history"),
        "recommendation": reverse("recommendation")
    }


def __get_recommendation_history(request):
    user = request.user
    if user:
        sessions = user.session_set.all()
        recommendations = Recommendation.objects.filter(session__in=sessions)
        if recommendations:
            return recommendations
