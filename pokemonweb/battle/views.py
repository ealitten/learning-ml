from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from .forms import PokemonForm

def index(request):
    return render(request, 'battle/index.html', {})

def pokemon(request):
    return render(request, 'battle/pokemon.html', {})

def pokemon_data(request):
    all_pokemon = Pokemon.objects.all() 
    selected = request.POST.get('pk1')
    selected_2 = request.POST.get('pk2')
    data = {'all_pokemon': all_pokemon, 'selected': selected, 'selected_2': selected_2}
    return render(request, 'battle/pokemon_data.html', data)

def pokemon_details(request):
    print("Inside pokemon_details")
    pid = request.GET.get('pid')
    if pid is None:
        return ''
    else:
        details = Pokemon.objects.get(uid=pid)
        data = {'details': details}
        return render(request, 'battle/pokemon_details.html', data)