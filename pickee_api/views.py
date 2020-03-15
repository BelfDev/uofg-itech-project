import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Temporary renders login.html
def user_login(request):
    if request.method == 'POST':
        # Retrieves username and password
        username = request.POST['username']
        password = request.POST['password']
        # Authenticates the user
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                # If valid, log in the user
                login(request, user)
                return redirect('index')
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
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
    return redirect('index')
