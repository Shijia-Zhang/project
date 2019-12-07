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

<<<<<<< HEAD
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
=======

def stats(request): 
    total_count = Squirrel.objects.all().count() 
    running_true = Squirrel.objects.filter(running=True).count() 
    running_false = Squirrel.objects.filter(running=False).count() 
    running_pct = "{:.2%}".format(running_true/total_count) 
    chasing_true = Squirrel.objects.filter(chasing=True).count() 
    chasing_false = Squirrel.objects.filter(chasing=False).count() 
    chasing_pct = "{:.2%}".format(chasing_true/total_count) 
    climbing_true = Squirrel.objects.filter(climbing=True).count() 
    climbing_false = Squirrel.objects.filter(climbing=False).count() 
    climbing_pct = "{:.2%}".format(climbing_true/total_count) 
    eating_true = Squirrel.objects.filter(eating=True).count() 
    eating_false = Squirrel.objects.filter(eating=False).count() 
    eating_pct = "{:.2%}".format(eating_true/total_count) 
    foraging_true = Squirrel.objects.filter(foraging=True).count() 
    foraging_false = Squirrel.objects.filter(foraging=False).count() 
    foraging_pct = "{:.2%}".format(foraging_true/total_count) 
    context = { 
            'total_count' : total_count, 
            'running_true' : running_true, 
            'running_false' : running_false, 
            'running_pct' : running_pct, 
            'chasing_true' : chasing_true, 
            'chasing_false': chasing_false, 
            'chasing_pct' : chasing_pct, 
            'climbing_true' : climbing_true, 
            'climbing_false': climbing_false, 
            'climbing_pct' : climbing_pct, 
            'eating_true' : eating_true, 
            'eating_false': eating_false, 
            'eating_pct' : eating_pct, 
            'foraging_true' : foraging_true, 
            'foraging_false': foraging_false, 
            'foraging_pct' : foraging_pct, 
            } 
    return render(request, 'squirrel/stats.html',context)

>>>>>>> 20bd6772415be681e161a86efe1221e3f6c68f0e
