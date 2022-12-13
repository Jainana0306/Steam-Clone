from django.shortcuts import render, redirect
from .forms import GameForm, UserRegisterForm, GenreForm
from .models import Game, Genre
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
    return render(request, 'steamClone/Register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'steamClone/Profile-Login.html')


def cart(request):
    return render(request, 'steamClone/Cart-Login.html')


def add(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = GameForm()
        else:
            game = Game.objects.get(pk=id)
            form = GameForm(instance=game)
        return render(request, "steamClone/Add-Admin.html", {'form': form})
    else:
        if id == 0:
            form = GameForm(request.POST)
        else:
            game = Game.objects.get(pk=id)
            form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
        return redirect('/gameList')


def gameList(request):
    context = {'gameList': Game.objects.all()}
    return render(request, 'steamClone/Edit-Admin.html', context)


def delete(request, id):
    game = Game.objects.get(pk=id)
    game.delete()
    return redirect('/gameList')


def genreAdd(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = GenreForm()
        else:
            genre = Genre.objects.get(pk=id)
            form = GenreForm(instance=genre)
        return render(request, "steamClone/Genre-Admin.html", {'form': form})
    else:
        if id == 0:
            form = GenreForm(request.POST)
        else:
            genre = Genre.objects.get(pk=id)
            form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
        return redirect('/gameList')


def genreDelete(request, id):
    genre = Genre.objects.get(pk=id)
    genre.delete()
    return redirect('/gameList')
