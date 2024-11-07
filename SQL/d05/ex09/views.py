from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import Planets, People
import json


def find_planet(i):
    with open('ex09/data/ex09_initial_data.json', 'r') as f:
        data = json.load(f)
        for j in data:
            if j['pk'] == i['fields']['homeworld']:
                return j['fields']['name']


def display(request):
    people = People.objects.all()
    planets = Planets.objects.all()
    people.delete()
    planets.delete()
    try:
        with open('ex09/data/ex09_initial_data.json', 'r') as f:
            data = json.load(f)
            for i in data:
                if i['model'] == 'ex09.planets':
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
                elif i['model'] == 'ex09.people':
                    # print('hello')
                    # print(i['pk'])
                    # print(i['fields']['name'])
                    # print(i['fields']['homeworld'])
                    # print(find_planet(i))
                    # print('')
                    
                    if not i['fields']['homeworld']:
                        # print('None detected')
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
                        # print('None not detected')
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
    except Exception as e:
        return HttpResponse(e)
    

    people = People.objects.all()
    planets = Planets.objects.all()
    names = []
    
    
    for i in people:
        for j in planets:
            if i.homeworld and j.name == i.homeworld.name:
                climate = str(j.climate)
                if 'windy' in climate:
                    names.append(i.name)
        
    if not names:
        return HttpResponse('No data available, please use the following command to populate the database: python manage.py loaddata ex09/data/ex09_initial_data.json')
    
    names = sorted(names)
    
    return render(request, 'ex09/display.html', {'names': names})

