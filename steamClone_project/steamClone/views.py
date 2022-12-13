from django.shortcuts import render, redirect
from .forms import GameForm, UserRegisterForm, GenreForm
from .models import Game, Genre
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


class NullGame():
    id = 0
    name = 'null'
    description = 'null'
    genre = 'null'
    price = 0
    poster = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Empty_set_symbol.svg/640px-Empty_set_symbol.svg.png'


def main(request):

    objectAll = Game.objects.all()
    nullGame = NullGame
    gameList = [x for x in objectAll]
    try:
        context = {
            'game1': gameList[0],
            'game2': gameList[1],
            'game3': gameList[2],
            'game4': gameList[3],
        }
    except:
        try:
            context = {
                'game1': gameList[0],
                'game2': gameList[1],
                'game3': gameList[2],
                'game4': nullGame,
            }
        except:
            try:
                context = {
                    'game1': gameList[0],
                    'game2': gameList[1],
                    'game3': nullGame,
                    'game4': nullGame,
                }
            except:
                try:
                    context = {
                        'game1': gameList[0],
                        'game2': nullGame,
                        'game3': nullGame,
                        'game4': nullGame,
                    }
                except:
                    context = {
                        'game1': nullGame,
                        'game2': nullGame,
                        'game3': nullGame,
                        'game4': nullGame,
                    }
    return render(request, 'steamClone/Main.html', context)


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


def detail(request, id=0):
    if id == 0:
        return render(request, "steamClone/Detail.html", {'game': NullGame})
    game = Game.objects.get(pk=id)
    return render(request, "steamClone/Detail.html", {'game': game})


@login_required()
def profile(request):
    objectAll = Game.objects.all()
    nullGame = NullGame
    gameList = [x for x in objectAll]
    try:
        context = {
            'game1': gameList[0],
            'game2': gameList[1],
            'game3': gameList[2],
            'game4': gameList[3],
        }
    except:
        try:
            context = {
                'game1': gameList[0],
                'game2': gameList[1],
                'game3': gameList[2],
                'game4': nullGame,
            }
        except:
            try:
                context = {
                    'game1': gameList[0],
                    'game2': gameList[1],
                    'game3': nullGame,
                    'game4': nullGame,
                }
            except:
                try:
                    context = {
                        'game1': gameList[0],
                        'game2': nullGame,
                        'game3': nullGame,
                        'game4': nullGame,
                    }
                except:
                    context = {
                        'game1': nullGame,
                        'game2': nullGame,
                        'game3': nullGame,
                        'game4': nullGame,
                    }
    return render(request, 'steamClone/Profile-Login.html', context)


@login_required()
def cart(request):
    return render(request, 'steamClone/Cart-Login.html')


@login_required()
def add(request, id=0):
    if not request.user.is_superuser:
        return redirect('/')
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


@login_required()
def gameList(request):
    if not request.user.is_superuser:
        return redirect('/')
    context = {'gameList': Game.objects.all()}
    return render(request, 'steamClone/Edit-Admin.html', context)


@login_required()
def delete(request, id):
    if not request.user.is_superuser:
        return redirect('/')
    game = Game.objects.get(pk=id)
    game.delete()
    return redirect('/gameList')


@login_required()
def genreAdd(request, id=0):
    if not request.user.is_superuser:
        return redirect('/')
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


@login_required()
def genreDelete(request, id):
    if not request.user.is_superuser:
        return redirect('/')
    genre = Genre.objects.get(pk=id)
    genre.delete()
    return redirect('/gameList')
