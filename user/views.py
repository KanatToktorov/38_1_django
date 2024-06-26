from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from user.forms import RegisterForm, LoginForm, ProfileUpdateForm
from user.models import Users


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', {'form': form})

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        age = form.cleaned_data.get('age')
        bio = form.cleaned_data.get('bio')
        avatar = form.cleaned_data.get('avatar')

        Users.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            bio=bio,
            avatar=avatar
        )

        return redirect('/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {'form': form})

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)  # User Object or None

        if user is None:
            form.add_error(None, 'Пользователь не найден!')
            return render(request, 'user/login.html', {'form': form})

        login(request, user)  # Записывает session_key в Cookie

        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/auth/login/')
def profile_view(request):
    return render(request, 'user/profile.html')

def profile_update_view(request):
    if request.method == 'GET':
        profile = Users.objects.get(username=request.user.username)
        form = ProfileUpdateForm(instance=profile)
        return render(request, 'user/profile_update.html', {'form': form})

    if request.method == 'POST':
        profile = Users.objects.get(username=request.user.username)
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if not form.is_valid():
            return render(request, 'user/profile_update.html', {'form': form})

        form.save()
        return redirect('profile')


