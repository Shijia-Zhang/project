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
            return redirect(f'/squirrel/sighting/')
    if request.method == 'GET':
        form = SquirrelForm(request.GET)
        if form.is_valid():
            form.save()
            return resirect(f'/squirrel/sithing/')
    else:
        form = SquirrelForm()

    context = {
            'form': form,
            'jazz': True,
    }

    return render(request, 'squirrel/edit.html', context)
