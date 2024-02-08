from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    args = {
        'name': 'Nicolás Sanchez'
    }
    return render(request, 'home.html', args)

def about(request):
    return HttpResponse("<h1>Welcome to About Us</h1>")