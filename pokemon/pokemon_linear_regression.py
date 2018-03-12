import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

def main(argv):

  FEATURES = ["First_pokemon", "Second_pokemon"]
  LABEL = ["Winner"]


  def load_data():
    """Loads sanitised data"""
    data = pd.read_csv("./pokemon-challenge/full_pokemon_data.csv")
    train_data, test_data = train_test_split(data, test_size=0.2)

    return train_data, test_data

  pokemon_types = [ "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting",
   "Fire","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water" ]

  def build_model_columns():
    """Builds a set of feature columns for the model to use"""
    pokemon_1 = tf.feature_column.numeric_column('First_pokemon')
    pokemon_2 = tf.feature_column.numeric_column('Second_pokemon')
    pokemon_type_1 = tf.feature_column.categorical_column_with_vocabulary_list('p1_Type1', pokemon_types )
    pokemon_type_2 = tf.feature_column.categorical_column_with_vocabulary_list('p2_Type1', pokemon_types )
    p1_hp = tf.feature_column.numeric_column("p1_HP")
    p2_hp = tf.feature_column.numeric_column("p2_HP")
    feature_columns = [pokemon_1, pokemon_2, pokemon_type_1, pokemon_type_2, p1_hp, p2_hp]

    return feature_columns


  def input_fn(data_set, shuffle, batch_size, num_epochs=None):
    """Builds input fn which feeds data into model as tensors"""
    features = data_set[FEATURES]
    labels = data_set[LABEL]
    return tf.estimator.inputs.pandas_input_fn(
        x = features,
        y = labels,
        batch_size=batch_size,
        num_epochs=num_epochs,
        shuffle=shuffle,
        num_threads=1)


  def json_serving_input_fn():
    """Builds serving input fn which is used when model is running in cloud"""
    inputs = {}
    for feat in INPUT_COLUMNS:
      inputs[feat.name] = tf.placeholder(shape=[None], dtype=feat.dtype)
      
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)


  train_data, test_data = load_data()
  INPUT_COLUMNS = build_model_columns()

  # Build a Linear classifier which chooses between two classes (p1 win/p2 win)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = INPUT_COLUMNS,
    n_classes = 2)

  # Train the classifier using 80% of the data
  classifier.train(
    input_fn=input_fn(data_set=train_data, shuffle=True, batch_size=100, num_epochs=None),
    steps=2000
  )

  # Use the remaining 20% of data to evaluate accuracy
  eval_results = classifier.evaluate(
    input_fn=input_fn(data_set=test_data, shuffle=False, batch_size=100, num_epochs=1)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

  # Export SavedModel for upload to the cloud (Google ML engine)
  classifier.export_savedmodel('./', json_serving_input_fn)

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)
