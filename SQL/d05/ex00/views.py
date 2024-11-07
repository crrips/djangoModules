from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def init(request):
    conn = psycopg2.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'djangotraining',
        user = 'djangouser',
        password = 'secret',
    )
    
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            CREATE TABLE ex00_movies (
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
    