from django import forms
from .models import Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'description', 'genre', 'price', 'poster')
        labels = {
            'name': 'Game Name...',
            'description': 'Description...',
            'price': 'Price...',
        }

    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Select"
        self.fields['description'].required = False


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
