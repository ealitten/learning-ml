# Technical documentation for We Predicted That pokemon battle predictor

## Step ?? - Authenticating the request to Google ML engine on Heroku

Google API client first looks for an environment var GOOGLE_APPLICATION_CREDENTIALS, which it expects to be set as the path of a json file containing the service account details. You can also manually load credentials from file:

```credentials = service_account.Credentials.from_service_account_file('path/to/file.json')```

Since we're using Heroku, we can't include a credentials file without committing it to github (bad), so we have to find a way to load all info from Heroku env vars. Digging around in the [google-auth source code](https://github.com/GoogleCloudPlatform/google-auth-library-python/blob/master/google/oauth2/service_account.py) provides a clue.

You can load credentials from an in-memory stream, in case you have the file loaded already, with `service_account.Credentials.from_service_account_info`. We can therefore build a json file ourselves from Heroku environment variables instead loading the file!

