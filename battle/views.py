import json
import os

import googleapiclient.discovery
from django.http import HttpResponse
from django.shortcuts import render
from google.oauth2 import service_account

from .forms import PokemonForm
from .models import Pokemon

def pokemon_data(request):
    all_pokemon = Pokemon.objects.all()
    selected = request.POST.get('pk1')
    selected_2 = request.POST.get('pk2')
    data = {'all_pokemon': all_pokemon,
            'selected': selected, 'selected_2': selected_2}
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
    instances = [{"First_pokemon": p1.uid, "Second_pokemon": p2.uid, "p1_Type1":
                  p1.type_1, "p2_Type1": p2.type_1, "p1_HP": p1.hp, "p2_HP": p2.hp, "p1_Attack": p1.attack,
                  "p1_Defense": p1.defense, "p1_SpAtk": p1.sp_attack, "p1_SpDef": p1.sp_defense, "p1_Speed": p1.speed, "p2_Attack": p2.attack,
                  "p2_Defense": p2.defense, "p2_SpAtk": p2.sp_attack, "p2_SpDef": p2.sp_defense, "p2_Speed": p2.speed}]
    winner = json_request(instances)
    probabilities = winner[0]["probabilities"]
    p1_prob = probabilities[0]
    p2_prob = probabilities[1]
    result = {"probabilities": probabilities, "p1": p1.name, "p2": p2.name,
              "p1_prob": (round(p1_prob * 100)), "p2_prob": (round(p2_prob * 100))}
    return render(request, 'battle/winner.html', result)


# def json_request(instances):
#     project = 'elegant-beach-197514'
#     model = 'pokemon_predictor'
#     instances = instances
#     version = 'v10'

#     service_acc_info = {}
#     service_acc_info["type"] = "service_account"
#     service_acc_info["project_id"] = "elegant-beach-197514"
#     service_acc_info["private_key_id"] = os.environ.get("private_key_id")
#     print(service_acc_info)
#     service_acc_info["private_key"] = os.environ.get("private_key").replace('\\n', '\n')
#     print(service_acc_info)
#     service_acc_info["client_email"] = os.environ.get("client_email")
#     service_acc_info["client_id"] = os.environ.get("client_id")
#     service_acc_info["auth_uri"] = "https://accounts.google.com/o/oauth2/auth"
#     service_acc_info["token_uri"] = "https://accounts.google.com/o/oauth2/token"
#     service_acc_info["auth_provider_x509_cert_url"] = "https://www.googleapis.com/oauth2/v1/certs"
#     service_acc_info["client_x509_cert_url"] = os.environ.get(
#         "client_x509_cert_url")

    
#     credentials = service_account.Credentials.from_service_account_info(
#         service_acc_info)

#     service = googleapiclient.discovery.build(
#         "ml", "v1", credentials=credentials)
#     name = "projects/{}/models/{}".format(project, model)

#     if version is not None:
#         name += "/versions/{}".format(version)

#     response = service.projects().predict(
#         name=name,
#         body={"instances": instances}
#     ).execute()

#     if "error" in response:
#         raise RuntimeError(response["error"])

#     return (response["predictions"])
