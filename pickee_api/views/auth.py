from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework import viewsets
from django.http import JsonResponse

from pickee_api.serializers import UserSerializer


# Temporary renders login.html
# TODO: replace this by the Login Vue App
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            data = {
                'name': 'Yo Anton'
            }
            return JsonResponse(data)
    else:
        return render(request, 'login.html')


# Temporary renders signup.html
# TODO: replace this by the SignUp Vue App
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
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)


# Temporary serializer example
# TODO: remove this after creating other API views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
