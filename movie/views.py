from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    args = {
        'name': 'Nicolás Sanchez'
    }
    return render(request, 'home.html', args)

def about(request):
    return render(request, 'about.html')