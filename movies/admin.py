"""Module providing a function printing python version."""
from django.contrib import admin

# Register your models here.
from .models import Movie
admin.site.register(Movie)
