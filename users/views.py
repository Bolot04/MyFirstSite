from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm, UserProfileForm


def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})


def register_view(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': RegisterForm})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('/login/')
        else:
            return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': LoginForm})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)  # authenticate - проверяет на наличие users в БД
            if user is not None:
                login(request, user)
                return redirect('/product/')
            else:
                form.add_error('username', 'Invalid username or password')
        return render(request, 'users/login.html', {'form': LoginForm})


def logout_view(request):
    logout(request)
    return redirect('/category/')


def user_profile_view(request):
    user_profile = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile_update.html', {"form": form})
