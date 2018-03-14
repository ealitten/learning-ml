# Technical documentation for We Predicted That pokemon battle predictor

## Step 1- Data Munging

The first step of any machine learning project is "data munging", i.e. ensuring that your dataset is suitable for feeding into your model. This includes filling in gaps in the data (or removing columns if they are too incomplete), sorting the data, filtering, standardising, etc.

Fortunately for us, the Pokemon dataset we used was mostly complete - only one Pokemon name was missing so this could be filled in manually. However, the data was broken into multiple tables: `combats`, `pokemon_data` and `tests`. The `combats` table contained two pokemon ids, and the winner:

```
First_pokemon,Second_pokemon,Winner
266,298,298
702,701,701
191,668,668
...
````

As mentioned above, predicted a winner in a fight between two pokemon is a binary classification problem, since there are only two outcomes. In this dataset, the winner is identified by their id so there are 800 outcomes! The first step was therefore to identify the winner relative to the pokemon fighting so we have either pokemon 1 (0) or pokemon 2 (1) as the winner. The data munging was done in the terminal, rather than saved as a script, since it was a one-off process:

- Storing ‘combats.csv(win/lose data)’ file data into a dataframe variable data
```
import pandas as pd
data = pd.read_csv('./pokemon-challenge/combats.csv')
```

- To replace winner/loser pokemon id with 0 and 1, loop over data rows
```
for index, row in data.iterrows():
 if row['First_pokemon'] == row['Winner']:
   row['Winner'] = 0
 else
   row['Winner'] = 1
```

- Writing updated data (where Winner=0,Loser=1) to 'combats_relative_winner.csv'
```
data.to_csv(path_or_buf='combats_relative_winner.csv', index=False)
```

- Storing ‘combats_relative_winner.csv’ file data into a dataframe variable combats
```
combats = pd.read_csv('./pokemon-challenge/combats_relative_winner.csv')
```

This produced a nice table of relative winners:

```
First_pokemon,Second_pokemon,Winner
266,298,1
702,701,1
191,668,1
```

Our second problem was that the `combats` table only contained two possible features: pokemon 1 and pokemon 2. Using only this data produced a model that was only ~52% accurate, so we clearly needed to use more of the data available to improve predictions. This involved merging the data from `pokemon_data` table into `combats` twice - once for each pokemon, to produce a table where a single row contains all the details of both combatants:


- Storing first pokemon data (‘p1_pokemon.csv') into a dataframe  variable p1_data
```
p1_data = pd.read_csv('./pokemon-challenge/p1_pokemon.csv')
```

- Storing second pokemon data (‘p2_pokemon.csv') into a dataframe  variable p2_data
```
p2_data = pd.read_csv('./pokemon-challenge/p2_pokemon.csv')
```

- Merging the data of both first and second pokemon into one file
```
combats_with_both = pd.merge(combats_player_1, p2_data, on='Second_pokemon')
```

- Writing combats data of pokemons into 'full_pokemon_data.csv'
```
combats_with_both.to_csv(path_or_buf='full_pokemon_data.csv', index=False)
```

The end result can be seen in `full_pokemon_data` table.