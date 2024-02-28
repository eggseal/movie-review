from django.shortcuts import render
import matplotlib.pyplot as plot
import matplotlib
import io
import urllib, base64

from .models import Movie

# Create your views here.
def home(request):
    search = request.GET.get('search') or ""
    movies = Movie.objects.filter(title__contains=search)
    args = {
        'search': search,
        'movies': movies
    }
    return render(request, 'home.html', args)

def about(request):
    return render(request, 'about.html')

def statistics(request):
    matplotlib.use('Agg')
    movies = Movie.objects.all()

    movies_year = {}
    movies_genre = {}
    for movie in movies:
        year = movie.year or 'None'
        genre = movie.genre.split(',')[0] if movie.genre else 'None'
        movies_year[year] = movies_year[year] + 1 if year in movies_year else 1
        movies_genre[genre] = movies_genre[genre] + 1 if genre in movies_genre else 1

    bar_width = 0.5
    bar_posy = range(len(movies_year))
    bar_posg = range(len(movies_genre))

    # Movies by year plot
    plot.bar(bar_posy, movies_year.values(), width=bar_width, align='center')

    plot.title('Movies by Year')
    plot.xlabel('Year')
    plot.ylabel('Number of Movies')
    plot.xticks(bar_posy, movies_year.keys(), rotation=90)

    plot.subplots_adjust(bottom=0.3)

    buffery = io.BytesIO()
    plot.savefig(buffery, format='png')
    buffery.seek(0)
    plot.close()

    image_y = buffery.getvalue()
    buffery.close()
    graphic_y = base64.b64encode(image_y).decode('utf-8')

    # Movies by genre plot
    plot.bar(bar_posg, movies_genre.values(), width=bar_width, align='center')

    plot.title('Movies by Genre')
    plot.xlabel('Genre')
    plot.ylabel('Number of Movies')
    plot.xticks(bar_posg, movies_genre.keys(), rotation=90)

    plot.subplots_adjust(bottom=0.3)

    bufferg = io.BytesIO()
    plot.savefig(bufferg, format='png')
    bufferg.seek(0)
    plot.close()

    image_g = bufferg.getvalue()
    bufferg.close()
    graphic_g = base64.b64encode(image_g).decode('utf-8')

    return render(request, 'statistics.html', {'graphic_year': graphic_y, 'graphic_genre': graphic_g})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
    