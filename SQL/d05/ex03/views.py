from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import Movies
from django.shortcuts import get_object_or_404


def populate(request):
    movies = [
        Movies(title='The Phantom Menace', episode_nb=1, director='George Lucas', producer='Rick McCallum', release_date='1999-05-19'),
        Movies(title='Attack of the Clones', episode_nb=2, director='George Lucas', producer='Rick McCallum', release_date='2002-05-16'),
        Movies(title='Revenge of the Sith', episode_nb=3, director='George Lucas', producer='Rick McCallum', release_date='2005-05-19'),
        Movies(title='A New Hope', episode_nb=4, director='George Lucas', producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25'),
        Movies(title='The Empire Strikes Back', episode_nb=5, director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17'),
        Movies(title='Return of the Jedi', episode_nb=6, director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25'),
        Movies(title='The Force Awakens', episode_nb=7, director='J.J. Abrams', producer='Kathleen Kennedy, J.J. Abrams, Bryan Burk', release_date='2015-12-11'),
    ]
    
    for movie in movies:
        try:
            movie.save()
        except Exception as e:
            return HttpResponse(e.args)
    
    return HttpResponse('OK')
    
    
def display(request):
    queryset = Movies.objects.all()
    titles = list(queryset)
    movies = []
    
    for title in titles:
        movies.append(get_object_or_404(Movies, title=title))
    
    if not movies:
        return HttpResponse('No data available')
    
    return render(request, 'ex03/index.html', {'movies': movies})
