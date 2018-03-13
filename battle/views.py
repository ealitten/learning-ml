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
    pid = request.GET.get('pid')
    if pid is None:
        return ''
    else:
        details = Pokemon.objects.get(uid=pid)
        data = {'details': details}
        return render(request, 'battle/pokemon_details.html', data)

def fight(request):
    p1 = request.POST.get('pk1_id')
    p2 = request.POST.get('pk2_id')
    details_1 = Pokemon.objects.get(uid=pokemon_1)
    details_2 = Pokemon.objects.get(uid=pokemon_2)
    instances = [{"First_pokemon": p1,"Second_pokemon": p2,"p1_Type1":
    " Fighting","p2_Type1": " Water","p1_HP": 65,"p2_HP": 170,"p1_Attack": 125,
    "p1_Defense": 60,"p1_SpAtk": 95,"p1_SpDef": 60,"p1_Speed": 105,"p2_Attack": 90,
    "p2_Defense": 45,"p2_SpAtk": 90,"p2_SpDef": 45,"p2_Speed": 60}]
    print(details_1)
    print(details_2)
