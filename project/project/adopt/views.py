from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Pet
from .forms import PetForm

def all_pets(request):
    pets = Pet.objects.all()
    context = {
         'pets': pets,
    }
    return render(request, 'adopt/all.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(f"{pet.id}")

def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        # check form data
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/{pet_id}')
    else:
         form = PetForm(instance=pet)
    context = { 
            'form': form,
    }
    return render(request, 'adopt/edit.html', context)

def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST,instance = pet)
        if form.is_valid():
            form.save()
            return redirect('/adopt/list')
    else:
        form = PetForm(instance=pet)
    context = {
            'form': form,
    }
    return render(request, 'adopt/edit.html', context)
