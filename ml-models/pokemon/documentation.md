
## Step 1- Data Munging

import pandas as pd

Storing ‘combats.csv(win/lose data)’ file data into a dataframe variable data
```
data = pd.read_csv('./pokemon-challenge/combats.csv')
```

To replace winner/loser pokemon id with 0 and 1, loop over data rows
```
for index, row in data.iterrows():
 if row['First_pokemon'] == row['Winner']:
   row['Winner'] = 0
 else
   row['Winner'] = 1
```

Writing updated data( where Winner=0,Loser=1) to 'combats_relative_winner.csv'
```
data.to_csv(path_or_buf='combats_relative_winner.csv', index=False)
```

Storing ‘combats_relative_winner.csv’ file data into a dataframe variable combats
```
combats = pd.read_csv('./pokemon-challenge/combats_relative_winner.csv')
```

Storing first pokemon data (‘p1_pokemon.csv') into a dataframe  variable p1_data
```
p1_data = pd.read_csv('./pokemon-challenge/p1_pokemon.csv')
```

Storing second pokemon data (‘p2_pokemon.csv') into a dataframe  variable p2_data
```
p2_data = pd.read_csv('./pokemon-challenge/p2_pokemon.csv')
```

Merging the data of both first and second pokemon into one file
```
combats_with_both = pd.merge(combats_player_1, p2_data, on='Second_pokemon')
```

Writing combats data of pokemons into 'full_pokemon_data.csv'
```
combats_with_both.to_csv(path_or_buf='full_pokemon_data.csv', index=False)
```

## Step ? - Exporting & uploading the model

1. Add code to py file to export the saved model once training is finished:

```
classifier.export_savedmodel('./export/', json_serving_input_fn)
```

2. Copy saved model folder (e.g. 15208652) to google storage bucket

3. Create version of model from the saved model folder

```
gcloud ml-engine models versions create v10 —model pokemon_predictor --origin gs://wepredictedthat-pokemon/export/15208652 --runtime-version 1.4
```

4. Sending a test query to the ML engine
  ```
  gcloud ml-engine predict --model pokemon_predictor --version v10 --json-instances test_query.json
  ```

## Step ?? - Authenticating the request to Google ML engine on Heroku


Google API client first looks for an environment var GOOGLE_APPLICATION_CREDENTIALS, which it expects to be set as the path of a json file containing the service account details. You can also manually load credentials from file:

```credentials = service_account.Credentials.from_service_account_file('path/to/file.json')```

Since we're using Heroku, we can't include a credentials file without committing it to github (bad), so we have to find a way to load all info from Heroku env vars. Digging around in the [google-auth source code](https://github.com/GoogleCloudPlatform/google-auth-library-python/blob/master/google/oauth2/service_account.py) provides a clue.

You can load credentials from an in-memory stream, in case you have the file loaded already, with `service_account.Credentials.from_service_account_info`. We can therefore build a json file ourselves from Heroku environment variables instead loading the file!