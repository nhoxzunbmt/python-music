- python manage.py migrate
- python manage.py makemigrations music
- python manage.py sqlmigrate music 0001
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py shell
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

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install pygments  # We'll be using this for the code highlighting
