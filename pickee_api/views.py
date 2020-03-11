from django.shortcuts import render


# Temporary renders login.html
# TODO: replace this by the Login Vue App
def login(request):
    response = render(request, 'login.html', context={})
    return response


# Temporary renders signup.html
# TODO: replace this by the SignUp Vue App
def signup(request):
    response = render(request, 'signup.html', context={})
    return response
