- virtualenv -p python3 .venv
- source .venv/bin/activate
- python manage.py migrate
- python manage.py makemigrations music
- python manage.py sqlmigrate music 0001
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py shell
- python manage.py show_urls
- sudo lsof -t -i tcp:8000 | xargs kill -9

>>> from music.models import Album,Song
>>> album1 = Album.objects.get(pk=1)
>>> song1 = Song()
>>> song1.song_title = "Be len ba tap 1"
>>> song1.file_type = "mp3"
>>> song1.album = album1
>>> song1.save()
>>> album1.song_set.all()
>>> album1.song_set.count()
>>> album1.song_set.create(song_title='I love bacon', file_type = 'mp3')

pip install django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install pygments  
pip install Faker
pip install arrow
pip install Celery
pip install virtualenv
pip install httpie
pip install djangorestframework-xml
pip install djangorestframework-jsonp
pip install djangorestframework-yaml
pip install coreapi
pip install coreapi-cli
pip install djangorestframework-jwt
pip install psycopg2-binary
pip install django_extensions
pip install django-cors-headers
pip install djangorestframework
pip install pygments


[DATE]
- https://arrow.readthedocs.io/en/latest/ 
[TASK-CRONJOB]
- http://www.celeryproject.org/
- https://scrapy.org/
- http://pygments.org/


http POST http://127.0.0.1:8000/api/users/login/ email="thanhloi@ringier.com.vn" password="ThanhLoi1993"

curl -X POST http://127.0.0.1:8000/api/users/login/ -d "email=thanhloi@ringier.com.vn&password=ThanhLoi1993"


rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate