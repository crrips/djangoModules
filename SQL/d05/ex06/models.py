from django.db import migrations

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunSQL(
            '''
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = NOW();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
            ''',
            reverse_sql='DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies; DROP FUNCTION IF EXISTS update_changetimestamp_column;'
        )
    ]
