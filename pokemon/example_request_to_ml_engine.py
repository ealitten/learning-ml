import argparse
import base64
import json

import googleapiclient.discovery
import six

# This requires the environment variable GOOGLE_APPLICATION_CREDENTIALS to be set to the path of a json file with the service account details

project = 'elegant-beach-197514'
model = 'pokemon_predictor'
instances = [{"First_pokemon": 682,"Second_pokemon": 352,"p1_Type1": " Fighting","p2_Type1": " Water","p1_HP": 65,"p2_HP": 170,"p1_Attack": 125,"p1_Defense": 60,"p1_SpAtk": 95,"p1_SpDef": 60,"p1_Speed": 105,"p2_Attack": 90,"p2_Defense": 45,"p2_SpAtk": 90,"p2_SpDef": 45,"p2_Speed": 60}]
version = 'v10'

service = googleapiclient.discovery.build('ml', 'v1')
name = 'projects/{}/models/{}'.format(project, model)

if version is not None:
    name += '/versions/{}'.format(version)

response = service.projects().predict(
    name=name,
    body={'instances': instances}
).execute()

if 'error' in response:
    raise RuntimeError(response['error'])

print(response['predictions'])