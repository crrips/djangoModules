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
            CREATE TABLE ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
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
    
    movies = [
        ('The Phantom Menace', 1, '', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        ('Attack of the Clones', 2, '', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        ('Revenge of the Sith', 3, '', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        ('A New Hope', 4, '', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        ('The Empire Strikes Back', 5, '', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        ('Return of the Jedi', 6, '', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        ('The Force Awakens', 7, '', 'J.J. Abrams', 'Kathleen Kennedy, J.J. Abrams, Bryan Burk', '2015-12-11'),
    ]
    
    for movie in movies:
        try:
            cursor.execute('''
                INSERT INTO ex04_movies (title, episode_nb, opening_crawl, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s, %s);
            ''', movie)
        except Exception as e:
            return HttpResponse(e.args)
    
    conn.commit()
    cursor.close()
    
    return HttpResponse('OK')
    
    
def display(request):
    conn = conn_db()
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM ex04_movies;')
    except Exception as e:
        return HttpResponse('No data available')
    
    movies = cursor.fetchall()
    
    if not movies:
        return HttpResponse('No data available')
    
    cursor.close()

    return render(request, 'ex04/display.html', {'movies': movies})


def remove(request):
    conn = conn_db()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                DELETE FROM ex04_movies WHERE title = %s;
            ''', (title,))
        except Exception as e:
            return HttpResponse(e.args)
        
        conn.commit()
        cursor.close()
        
        return HttpResponse('Movie removed')
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT title FROM ex04_movies;')
    except Exception as e:
        return HttpResponse('No data available')
    
    movie_names = cursor.fetchall()
    
    cursor.close()
    
    movie_names = [movie[0] for movie in movie_names]
    
    if not movie_names:
        return HttpResponse('No data available')
    
    return render(request, 'ex04/remove.html', {'movie_names': movie_names})
