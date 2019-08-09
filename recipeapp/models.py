from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,)
    description = models.CharField(max_length=400)
    time_required = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
