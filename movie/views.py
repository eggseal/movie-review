from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.
def home(request):
    search = request.GET.get('search')
    movies = Movie.objects.filter(title__contains=search)
    args = {
        'search': search,
        'movies': movies
    }
    return render(request, 'home.html', args)

def about(request):
    return render(request, 'about.html')