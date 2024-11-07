from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import Planets, People, Movies
import json
from datetime import datetime


def find_planet(i):
    with open('ex10/data/ex10_initial_data.json', 'r') as f:
        data = json.load(f)
        for j in data:
            if j['pk'] == i['fields']['homeworld']:
                return j['fields']['name']


def set_characters(pk):
    with open('ex10/data/ex10_initial_data.json', 'r') as f:
        data = json.load(f)
        characters = []
        for j in data:
            if j['model'] == 'ex10.people' and j['pk'] in pk:
                characters.append(j['fields']['name'])
        return characters


def display(request):
    people = People.objects.all()
    planets = Planets.objects.all()
    movies = Movies.objects.all()
    people.delete()
    planets.delete()
    movies.delete()
    try:
        with open('ex10/data/ex10_initial_data.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if i['model'] == 'ex10.planets':
                    planet = Planets(
                        name=i['fields']['name'],
                        climate=i['fields']['climate'],
                        diameter=i['fields']['diameter'],
                        orbital_period=i['fields']['orbital_period'],
                        population=i['fields']['population'],
                        rotation_period=i['fields']['rotation_period'],
                        surface_water=i['fields']['surface_water'],
                        terrain=i['fields']['terrain']
                    )
                    planet.save()
                elif i['model'] == 'ex10.people':
                    if not i['fields']['homeworld']:
                        people = People(
                            name=i['fields']['name'],
                            birth_year=i['fields']['birth_year'],
                            gender=i['fields']['gender'],
                            eye_color=i['fields']['eye_color'],
                            hair_color=i['fields']['hair_color'],
                            height=i['fields']['height'],
                            mass=i['fields']['mass']
                        )
                        people.save()
                    else:
                        people = People(
                            name=i['fields']['name'],
                            birth_year=i['fields']['birth_year'],
                            gender=i['fields']['gender'],
                            eye_color=i['fields']['eye_color'],
                            hair_color=i['fields']['hair_color'],
                            height=i['fields']['height'],
                            mass=i['fields']['mass'],
                            homeworld=Planets.objects.get(name=find_planet(i))
                        )
                        people.save()
                elif i['model'] == 'ex10.movies':
                    movie = Movies(
                        title=i['fields']['title'],
                        episode_nb=i['pk'],
                        opening_crawl=i['fields']['opening_crawl'],
                        director=i['fields']['director'],
                        producer=i['fields']['producer'],
                        release_date=i['fields']['release_date']
                    )
                    pk = i['fields']['characters']
                    characters = People.objects.filter(name__in=set_characters(pk))
                    movie.save()
                    movie.characters.add(*characters)
    except Exception as e:
        return HttpResponse(e)
    
    people = People.objects.all()
    planets = Planets.objects.all()
    movies = Movies.objects.all()
        
    genders = []
    for i in people:
        if not i.gender in genders:
            genders.append(i.gender)
    
    if request.method == 'POST':
        try:
            min_release_date = request.POST.get('min_release_date')
            min_release_date = datetime.strptime(min_release_date, "%Y-%m-%d").date()
            max_release_date = request.POST.get('max_release_date')
            max_release_date = datetime.strptime(max_release_date, "%Y-%m-%d").date()
            planet_diameter = request.POST.get('planet_diameter')
            planet_diameter = int(planet_diameter)
            gender = request.POST.get('gender')
        except Exception as e:
            return HttpResponse(e)
        
        results_movies = []
        results_characters = []
        
        for i in movies:
            if i.release_date >= min_release_date and i.release_date <= max_release_date:
                for j in i.characters.all():
                    if j.gender == gender and j.homeworld:
                        if j.homeworld.diameter and j.homeworld.diameter > planet_diameter:
                            results_characters.append(j)
                            results_movies.append(i)
        
        model_list = []
        for i in range(len(results_characters)):
            listik = [results_characters[i].name,
            results_characters[i].gender,
            results_movies[i].title,
            results_characters[i].homeworld.name,
            results_characters[i].homeworld.diameter]
            model_list.append(listik)
            
        if not model_list:
            return HttpResponse('No data available')
            
        return render(request, 'ex10/results.html', {'model_list': model_list})
        
    return render(request, 'ex10/display.html', {'genders': genders})

