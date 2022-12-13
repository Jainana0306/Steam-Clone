from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.FloatField()
    poster = models.URLField()
    url = models.URLField()
