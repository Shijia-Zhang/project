from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

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
            return redirect(f'/squirrel/sightings/')
    if request.method == 'GET':
        form = SquirrelForm(request.GET)
        if form.is_valid():
            form.save()
            return resirect(f'/squirrel/sighings/')
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
            return redirect(f'/squirrel/sightings/{unique_squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'squirrel/edit.html', context)
