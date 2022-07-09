from django.shortcuts import render
from .models import shrooms

# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shrooms_index(request):
    return render(request, 'shrooms/index.html', { 'shrooms': shrooms })
