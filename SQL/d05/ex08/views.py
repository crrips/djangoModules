from django.shortcuts import render
from django.http import HttpResponse
import psycopg2


def conn_db():
    return psycopg2.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'djangotraining',
        user = 'djangouser',
        password = 'secret',
    )


def init(request):
    conn = conn_db()
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            CREATE TABLE ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate TEXT,
                diametr INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
            );
        ''')
        
        conn.commit()
        cursor.close()
    except Exception as e:
        return HttpResponse(e.args)
    
    return HttpResponse('OK')
    
    
def populate(request):
    conn = conn_db()
    
    cursor = conn.cursor()
    
    try:
        with open('ex08/data/planets.csv', 'r', encoding="utf-8") as f:
            cursor.copy_expert('''
                COPY ex08_planets(name, climate, diametr, orbital_period, population, rotation_period, surface_water, terrain)
                FROM STDIN WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
            ''', f)
            
        with open('ex08/data/people.csv', 'r', encoding="utf-8") as f:
            cursor.copy_expert('''
                COPY ex08_people(name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                FROM STDIN WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
            ''', f)
    except Exception as e:
        return HttpResponse(e.args)
    
    conn.commit()
    cursor.close()
    
    return HttpResponse('OK')


def display(request):
    conn = conn_db()
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT ex08_people.name FROM ex08_people
            RIGHT JOIN ex08_planets ON ex08_people.homeworld = ex08_planets.name
            WHERE ex08_planets.climate LIKE '%windy' AND ex08_people.name IS NOT NULL
            ORDER BY ex08_people.name ASC;
                       ''')
    except Exception as e:
        return HttpResponse('No data available')
    
    names = cursor.fetchall()
    
    if not names:
        return HttpResponse('No data available')
    
    names = [name[0] for name in names]
    
    cursor.close()

    return render(request, 'ex08/display.html', {'names': names})

