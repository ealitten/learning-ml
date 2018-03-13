from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from .forms import PokemonForm

import os
import json

import googleapiclient.discovery
from google.oauth2 import service_account

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
    pokemon_1 = request.POST.get('pk1_id')
    pokemon_2 = request.POST.get('pk2_id')
    p1 = Pokemon.objects.get(uid=pokemon_1)
    p2 = Pokemon.objects.get(uid=pokemon_2)
    instances = [{"First_pokemon": p1.uid,"Second_pokemon": p2.uid,"p1_Type1":
    p1.type_1,"p2_Type1": p2.type_1,"p1_HP": p1.hp,"p2_HP": p2.hp,"p1_Attack": p1.attack,
    "p1_Defense": p1.defense,"p1_SpAtk": p1.sp_attack,"p1_SpDef": p1.sp_defense,"p1_Speed": p1.speed,"p2_Attack": p2.attack,
    "p2_Defense": p2.defense,"p2_SpAtk": p2.sp_attack,"p2_SpDef": p2.sp_defense,"p2_Speed": p2.speed}]
    winner = json_request(instances)
    probabilities = winner[0]["probabilities"]
    result = {"probabilities": "some text"}
    return render(request,'battle/winner.html', result)
   
def json_request(instances):
    project = 'elegant-beach-197514'
    model = 'pokemon_predictor'
    instances = instances
    version = 'v10' 
    credentials = service_account.Credentials.from_service_account_file("/Users/reenasharma/makers/we-predicted-that/battle/authentication.json")
    service = googleapiclient.discovery.build("ml", "v1", credentials=credentials)
    name = "projects/{}/models/{}".format(project, model)

    if version is not None:
        name += "/versions/{}".format(version)

    response = service.projects().predict(
        name=name,
        body={"instances": instances}
    ).execute()

    if "error" in response:
        raise RuntimeError(response["error"])

    return (response["predictions"])
