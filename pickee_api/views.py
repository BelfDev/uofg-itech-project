from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Temporary renders login.html
# TODO: replace this by the Login Vue App
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html')


# Temporary renders signup.html
# TODO: replace this by the SignUp Vue App
def user_signup(request):
    response = render(request, 'signup.html', context={})
    return response
