from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Count

from .models import Squirrel
from .forms import SquirrelForm

def index(request):
    return render(request, 'squirrel/index.html')

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels' : squirrels,
    }
    return render(request, 'squirrel/all.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm()

    context = {
            'form': form,
            'jazz': True,
    }

    return render(request, 'squirrel/edit.html', context)

def update_squirrel(request,unique_squirrel_ID):
    squirrel = Squirrel.objects.get(ID=unique_squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'squirrel/edit.html', context)

def map(request):
    squirrels = Squirrel.objects.order_by('?')[:100]
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'squirrel/map.html', context)

def stats(request): 
    total_count = Squirrel.objects.all().count() 
    running_true = Squirrel.objects.filter(running=True).count() 
    running_false = Squirrel.objects.filter(running=False).count()
    running_pct = "{:.2%}".format(running_true/total_count) 
    context = { 
            'total_count' : total_count, 
            'running_true' : running_true, 
            'running_false' : running_false,
            'running_pct' : running_pct, } 
    return render(request, 'squirrel/stats.html',context)
