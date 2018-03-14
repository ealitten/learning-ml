# Technical documentation for We Predicted That pokemon battle predictor

## Step 5 - Authenticating the request to Google ML engine on Heroku

Once we had our app deployed on Heroku, the next step was to enable it to request predictions from our model on Google ML engine. In [step 3]((https://github.com/ealitten/we-predicted-that/blob/master/docs/exporting_upload.md)) we described sending a request to the model and its response - however, this was sent from the machine where the model was developed, which had the gcloud SDK installed and was already authenticated. For server-to-server interactions, Google requires creation of a service account with limited permission. First we created a new service account, and gave it ML Developer permissions (required to request predictions), and then downloaded a JSON file containing the details including the private key.

The Google API client by default looks for an environment var GOOGLE_APPLICATION_CREDENTIALS, which it expects to be set as the path of a json file containing the service account details. Since we're using Heroku, we couldn't include a credentials file without committing it to github (a very bad idea as it exposes our private key). Heroku offers config variables, which function as environment variables and can be accessed the same way. However, how to deal with the Google API client expecting the auth details to be in a file? Digging around in the [google-auth source code](https://github.com/GoogleCloudPlatform/google-auth-library-python/blob/master/google/oauth2/service_account.py) provides a clue:

```
Or if you already have the service account file loaded::

    service_account_info = json.load(open('service_account.json'))
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info)
```

You can load credentials from an in-memory dictionary, in case you have the file loaded already, with `service_account.Credentials.from_service_account_info`. We can therefore build a json file ourselves from Heroku environment variables instead of loading the file! After some experimentation with \n characters, which Heroku sanitises in its config vars but which we don't want sanitised, we have a working implementation:

```python
  project = 'elegant-beach-197514'
  model = 'pokemon_predictor'
  instances = instances
  version = 'v10'

  service_acc_info = {}
  service_acc_info["type"] = "service_account"
  service_acc_info["project_id"] = "elegant-beach-197514"
  service_acc_info["private_key_id"] = os.environ.get("private_key_id")
  service_acc_info["private_key"] = os.environ.get("private_key").replace('\\n', '\n')
  service_acc_info["client_email"] = os.environ.get("client_email")
  service_acc_info["client_id"] = os.environ.get("client_id")
  service_acc_info["auth_uri"] = "https://accounts.google.com/o/oauth2/auth"
  service_acc_info["token_uri"] = "https://accounts.google.com/o/oauth2/token"
  service_acc_info["auth_provider_x509_cert_url"] = "https://www.googleapis.com/oauth2/v1/certs"
  service_acc_info["client_x509_cert_url"] = os.environ.get("client_x509_cert_url")

  credentials = service_account.Credentials.from_service_account_info(service_acc_info)

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
```



