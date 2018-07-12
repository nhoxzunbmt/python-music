- virtualenv -p python3 .venv
- source .venv/bin/activate 
- deactivate
- virtualenv -p python3 ~/.venv/music
- source ~/.venv/music/bin/activate
- find . -name "*.pyc" -exec git rm -f "{}" \;

- python3 manage.py makemigrations learn
- python3 manage.py migrate
- python3 manage.py sqlmigrate music 0001
- python3 manage.py createsuperuser
- python3 manage.py runserver
- python3 manage.py shell
- python3 manage.py show_urls
- sudo lsof -t -i tcp:8000 | xargs kill -9

Person.objects.create(first_name="foobar")
from music.models import Album,Song
album1 = Album.objects.get(pk=1)
song1 = Song()
song1.song_title = "Be len ba tap 1"
song1.file_type = "mp3"
song1.album = album1
song1.save()
album1.song_set.all()
album1.song_set.count()
album1.song_set.create(song_title='I love bacon', file_type ='mp3')


pip3 install django
pip3 install djangorestframework
pip3 install markdown       # Markdown support for the browsable API.
pip3 install django-filter  # Filtering support
pip3 install pygments  
pip3 install Faker
pip3 install arrow
pip3 install Celery
pip3 install virtualenv
pip3 install httpie
pip3 install djangorestframework-xml
pip3 install djangorestframework-jsonp
pip3 install djangorestframework-yaml
pip3 install coreapi
pip3 install coreapi-cli
pip3 install djangorestframework-jwt
pip3 install psycopg2-binary
pip3 install django_extensions
pip3 install django-cors-headers
pip3 install djangorestframework
pip3 install pygments


[DATE]
- https://arrow.readthedocs.io/en/latest/ 
[TASK-CRONJOB]
- http://www.celeryproject.org/
- https://scrapy.org/
- http://pygments.org/


http POST http://127.0.0.1:8000/api/users/login/ email="nhoxzunbmt@gmail.com" password="123456"

curl -X POST http://127.0.0.1:8000/api/users/login/ -d "email=nhoxzunbmt@gmail.com&password=123456"


rm -f db.sqlite3
rm -r snippets/migrations
python3 manage.py makemigrations snippets
python3 manage.py migrate