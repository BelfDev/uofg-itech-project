import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pickee_api.forms import PickeeUserCreationForm


def home(request):
    data = json.dumps({
        "user": get_user_data(request),
    })
    context = {'data': data}
    return render(request, 'home.html', context=context)


def recommendation(request):
    user = json.dumps(get_user_data(request))
    preferences = json.dumps(request.POST)
    context = { 'user': user, 'preferences': preferences}

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


@login_required
def profile(request):
    user_profile_data = {"age": request.user.age, "gender": request.user.gender}
    data = json.dumps({
        "user": {**get_user_data(request), **user_profile_data}
    });
    context = {'data': data}
    return render(request, 'profile.html', context=context)


@login_required
def history(request):
    return render(request, 'history.html')


@login_required
def preferences(request):
    return render(request, 'preferences.html')


# Helper methods

def __get_user_data(request):
    if not request.user.is_authenticated:
        return {}

    return {
        "id": request.user.id,
        "name": request.user.first_name,
        "email": request.user.email,
        "picture": request.user.picture.url if request.user.picture else None
    }
