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
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
