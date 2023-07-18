from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import DuoMathUser
from .forms import DuoMathUserForm
# Create your views here.


def user(request):
    return render(request, 'users/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = DuoMathUserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            if 'profile_pics' in request.FILES:
                user.profile_pics = request.FILES['profile_pics']
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = DuoMathUserForm()

    return render(request, 'users/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password, model=DuoMathUser)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password {password}")
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'users/login.html', {})
