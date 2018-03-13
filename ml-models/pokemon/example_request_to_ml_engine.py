import os
import json
import googleapiclient.discovery
from google.oauth2 import service_account

project = 'elegant-beach-197514'
model = 'pokemon_predictor'
instances = [{"First_pokemon": 682,"Second_pokemon": 352,"p1_Type1": " Fighting","p2_Type1": " Water","p1_HP": 65,"p2_HP": 170,"p1_Attack": 125,"p1_Defense": 60,"p1_SpAtk": 95,"p1_SpDef": 60,"p1_Speed": 105,"p2_Attack": 90,"p2_Defense": 45,"p2_SpAtk": 90,"p2_SpDef": 45,"p2_Speed": 60}]
version = 'v10'

# Google API client first looks for an environment var GOOGLE_APPLICATION_CREDENTIALS, which it expects to be set 
# as the path of a json file containing the service account details. You can also manually load credentials from file:

# credentials = service_account.Credentials.from_service_account_file('path/to/file.json')

# Since we're using Heroku, we can't include a credentials file without committing it to github (bad)
# so we have to find a way to load all info from Heroku env vars. Digging around in the google-auth source code provides a clue:
# https://github.com/GoogleCloudPlatform/google-auth-library-python/blob/master/google/oauth2/service_account.py
# You can load credentials from an in-memory stream, in case you have the file loaded already, with service_account.Credentials.from_service_account_info
# We can therefore build a json file ourselves from env variables instead loading the file

service_acc_info = {}

print(os.environ.get("private_key_id"))
print(os.environ.get("private_key"))
print(os.environ.get("client_email"))
print(os.environ.get("client_id"))
print(os.environ.get("client_x509_cert_url"))

service_acc_info["type"] = "service_account"
service_acc_info["project_id"] = "elegant-beach-197514"
service_acc_info["private_key_id"] = os.environ.get("private_key_id")
service_acc_info["private_key"] = os.environ.get("private_key")
service_acc_info["client_email"] = os.environ.get("client_email")
service_acc_info["client_id"] = os.environ.get("client_id")
service_acc_info["auth_uri"] = "https://accounts.google.com/o/oauth2/auth"
service_acc_info["token_uri"] = "https://accounts.google.com/o/oauth2/token"
service_acc_info["auth_provider_x509_cert_url"] = "https://www.googleapis.com/oauth2/v1/certs"
service_acc_info["client_x509_cert_url"] = os.environ.get("client_x509_cert_url")

credentials = service_account.Credentials.from_service_account_info(service_acc_info)

service = googleapiclient.discovery.build('ml', 'v1', credentials=credentials)
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