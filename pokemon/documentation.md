
import pandas as pd

## Step 1- Data Munging

# Storing ‘combats.csv(win/lose data)’ file data into a dataframe variable data
data = pd.read_csv('./pokemon-challenge/combats.csv')

# To replace winner/loser pokemon id with 0 and 1, loop over data rows-
for index, row in data.iterrows():
 if row['First_pokemon'] == row['Winner']:
   row['Winner'] = 0
 else:
   row['Winner'] = 1

# Writing updated data( where Winner=0,Loser=1) to 'combats_relative_winner.csv'
data.to_csv(path_or_buf='combats_relative_winner.csv', index=False)

# Storing ‘combats_relative_winner.csv’ file data into a dataframe variable combats
combats = pd.read_csv('./pokemon-challenge/combats_relative_winner.csv')

# Storing first pokemon data (‘p1_pokemon.csv') into a dataframe  variable p1_data
p1_data = pd.read_csv('./pokemon-challenge/p1_pokemon.csv')

# Storing second pokemon data (‘p2_pokemon.csv') into a dataframe  variable p2_data
p2_data = pd.read_csv('./pokemon-challenge/p2_pokemon.csv')

# Merging the data of both first and second pokemon into one file
combats_with_both = pd.merge(combats_player_1, p2_data, on='Second_pokemon')

# Writing combats data of pokemons into 'full_pokemon_data.csv'
combats_with_both.to_csv(path_or_buf='full_pokemon_data.csv', index=False)
