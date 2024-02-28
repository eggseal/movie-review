from django.core.management.base import BaseCommand
from movie.models import Movie
import json

class Command(BaseCommand):
    help='Load movies from movies.json into the Movie model'

    def handle(self, *args, **kwargs):
        file_path = 'movie/management/commands/movies.json'
        with open(file_path, 'r') as file:
            movies = json.load(file)
        
        for i in range(100):
            movie = movies[i]
            exists = Movie.objects.filter(title=movie['title']).first()
            if exists: continue

            Movie.objects.create(
                title=movie['title'],
                image='movie/images/default.jpg',
                genre=movie['genre'],
                year=movie['year']
            )