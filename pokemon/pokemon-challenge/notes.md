for index, row in data.iterrows():
...   if row['First_pokemon'] == row['Winner']:
...     row['Winner'] = 0
...   else:
...     row['Winner'] = 1
