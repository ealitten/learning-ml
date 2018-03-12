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
    selected = request.POST.get('pokemon_id')
    data = {'all_pokemon': all_pokemon, 'selected': selected}
    return render(request, 'battle/pokemon_data.html', data)

def pokemon_data_2(request):
    pk_id = request.GET.get('uid')
    nam = Pokemon.objects.filter(uid=pk_id).order_by('name')
    form = PokemonForm()
    return render(request, 'battle/pokemon_data.html', {'form': form, 'nam': nam})

