from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse

def movies(request):
    movies = Movies(title='The Phantom Menace', episode_nb=1, director='George Lucas', producer='Rick McCallum', release_date='1999-05-19')
    return HttpResponse(movies)
