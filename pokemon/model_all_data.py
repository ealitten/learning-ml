import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def load_csv(path):
    return pd.read_csv(path)


def add_suffix_to(dataframe, suffix):
    return dataframe.add_suffix(suffix)


def important_features(feature_data, classifier):
    effective = pd.DataFrame(
        {'feature_name': feature_data.columns.tolist()},
        {'feature_importance': classifier.feature_importances_})
    return effective.sort_values('feature_importance', ascending=False)


def build_frame(number):
    col1 = build_first_column(number)
    col2 = build_second_column(number)
    dataframe1 = pd.DataFrame({'First_pokemon': col1, 'Second_pokemon': col2})
    dataframe2 = pd.DataFrame({'First_pokemon': col2, 'Second_pokemon': col1})
    return pd.concat([dataframe1, dataframe2], ignore_index=True)


def build_first_column(number):
    maximum = number
    array = []
    for i in range(1, number + 1):
        array = array + [i] * (maximum - 1)
        maximum -= 1
    return array


def build_second_column(number):
    start = 2
    array = []
    for i in range(1, number):
        array = array + list(range(start, number + 1))
        start += 1
    return array


combats = load_csv('./pokemon-challenge/combats.csv')
pokemon = load_csv('./pokemon-challenge/pokemon.csv')
pokemon2 = pokemon.copy()
print('Loaded all data')

pokemon = add_suffix_to(pokemon, '_1')
pokemon2 = add_suffix_to(pokemon2, '_2')
print('Suffixes added')

merged = pd.merge(pokemon2, combats, left_on='#_2', right_on='Second_pokemon')
merged = pd.merge(pokemon, merged, left_on='#_1', right_on='First_pokemon')

merged['First_win'] = merged.apply(
    lambda x: 1 if x['First_pokemon'] == x['Winner'] else 0, axis=1)
print('Pokemon data merged, winners enumerated')

not_needed = [
    'First_pokemon',
    'Second_pokemon',
    '#_1',
    '#_2',
    'Type 1_1',
    'Type 2_1',
    'Type 1_2',
    'Type 2_2',
    'Name_1',
    'Name_2',
    'Legendary_1',
    'Legendary_2'
]

merged = merged.drop(not_needed + ['Winner'], axis=1)

x = merged.drop('First_win', axis=1)
y = merged['First_win']
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)
print('Data prepared')

random_forest = RandomForestClassifier(n_estimators=100, n_jobs=-1)
print('Started model training')
random_forest.fit(x_train, y_train)
acc_random_forest = round(random_forest.score(x_test, y_test) * 100, 1)
print('Model trained with:', acc_random_forest, '%', 'accuracy')

# This part is broken at the moment
# print('Important features:')
# print(important_features(x, random_forest))

print('Building dataframe for all battle combinations')
combinations = build_frame(800)
print('Combinations dataframe built')

print('Started preparing the combinations dataframe for predictions')
merged_combinations = pd.merge(pokemon2, combinations, left_on='#_2',
                               right_on='Second_pokemon')
merged_combinations = pd.merge(pokemon, merged_combinations,
                               left_on='#_1', right_on='First_pokemon')

merged_combinations = merged_combinations.drop(not_needed, axis=1)
print('Combinations dataframe prepared for predictions')

y_predict = random_forest.predict(merged_combinations)
print('Predictions made')

print('Preparing dataframe for saving to CSV')
final = pd.DataFrame({'First_pokemon': combinations['First_pokemon'],
                      'Second_pokemon': combinations['Second_pokemon'],
                      'First_win': y_predict})

winner = pd.DataFrame(final.apply(
    lambda x: x['First_pokemon'] if x['First_win'] == 1 else x['Second_pokemon'], axis=1), columns=['Winner'])
final = pd.concat([final, winner], axis=1)
final = final.drop(['First_win'], axis=1)

print('Finished, saving CSV')
final.to_csv(path_or_buf='./pokemon-challenge/all_predictions.csv', index=False)
print('Done')
