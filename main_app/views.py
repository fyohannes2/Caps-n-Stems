from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shroom
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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
    shroom = Shroom.objects.get(id=shroom_id)
    return render(request, 'shrooms/detail.html', { 'shroom': shroom})

def seasons(request):
    return render(request, 'shrooms/seasons/all.html')

def spring(request):
    bloom = Shroom.objects.all().filter(bloom_season='SPG')
    pick = Shroom.objects.all().filter(picking_season='SPG')
    return render(request, 'shrooms/seasons/spring.html', { 'bloom': bloom, 'pick': pick })

def summer(request):
    bloom = Shroom.objects.all().filter(bloom_season='SUM')
    pick = Shroom.objects.all().filter(picking_season='SUM')
    return render(request, 'shrooms/seasons/summer.html', { 'bloom': bloom, 'pick': pick })

def winter(request):
    bloom = Shroom.objects.all().filter(bloom_season='WIN')
    pick = Shroom.objects.all().filter(picking_season='WIN')
    return render(request, 'shrooms/seasons/winter.html', { 'bloom': bloom, 'pick': pick })

def fall(request):
    bloom = Shroom.objects.all().filter(bloom_season='FLL')
    pick = Shroom.objects.all().filter(picking_season='FLL')
    return render(request, 'shrooms/seasons/fall.html', { 'bloom': bloom, 'pick': pick })




def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ShroomCreate(LoginRequiredMixin, CreateView):
    model = Shroom
    fields = [ 'name',
        'scientific_name',
        'description',
        'type',
        'height',
        'spread',
        'bloom_season',
        'picking_season' ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class ShroomUpdate(LoginRequiredMixin, UpdateView):
    model = Shroom
    fields = ['scientific_name',
        'description',
        'type',
        'height',
        'spread',
        'bloom_season',
        'picking_season' ]
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(ShroomUpdate, self).dispatch(request, *args, **kwargs)

class ShroomDelete(LoginRequiredMixin, DeleteView):
    model = Shroom
    success_url = '/shrooms/'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(ShroomDelete, self).dispatch(request, *args, **kwargs)
