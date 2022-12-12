from django.shortcuts import render, redirect
from .forms import GameForm, UserRegisterForm
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def main(request):
    return render(request, 'steamClone/Main.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'steamClone/Register.html')  # , {'form': form}


@login_required()
def profile(request):
    return render(request, 'steamClone/Profile-Login.html')


def cart(request):
    return render(request, 'steamClone/Cart-Login.html')


def add(request):
    return render(request, 'steamClone/Add-Admin.html')


def edit(request):
    return render(request, 'steamClone/Edit-Admin.html')


def delete(request):
    return render(request, 'steamClone/Delete-Admin.html')
