from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shroom

# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shrooms_index(request):
    shrooms = Shroom.objects.all()
    return render(request, 'shrooms/index.html', { 'shrooms': shrooms })

def shrooms_detail(request, shroom_id):
    shroom  = Shroom.objects.get(id=shroom_id)
    return render(request, 'shrooms/detail.html', { 'shroom': shroom})

class ShroomCreate(CreateView):
    model = Shroom
    fields = '__all__'

class ShroomUpdate(UpdateView):
    model = Shroom
    fields = ['scientific_name',
        'description',
        'type',
        'height',
        'spread',
        'bloom_season',
        'picking_season' ]

class ShroomDelete(DeleteView):
    model = Shroom
    success_url = '/shrooms/' 
