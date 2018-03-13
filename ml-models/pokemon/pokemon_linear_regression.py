import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

def main(argv):

  FEATURES = ["First_pokemon", "Second_pokemon", 
              "p1_Type1", "p1_HP", "p1_Attack","p1_Defense","p1_SpAtk","p1_SpDef","p1_Speed", 
              "p2_Type1", "p2_HP", "p2_Attack","p2_Defense","p2_SpAtk","p2_SpDef","p2_Speed"
  ]

  LABEL = ["Winner"]

  def load_data():
    """Loads sanitised data and splits it between training & evaluation"""
    data = pd.read_csv("./pokemon-challenge/full_pokemon_data.csv")
    train_data, test_data = train_test_split(data, test_size=0.2)

    return train_data, test_data

  
  def build_model_columns():
    """Builds a set of feature columns for the model to use"""

    POKEMON_TYPES = [ "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting",
   "Fire","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water" ]

    pokemon_1 = tf.feature_column.numeric_column('First_pokemon')
    pokemon_2 = tf.feature_column.numeric_column('Second_pokemon')
    p1_type_1 = tf.feature_column.categorical_column_with_vocabulary_list('p1_Type1', POKEMON_TYPES )
    p2_type_1 = tf.feature_column.categorical_column_with_vocabulary_list('p2_Type1', POKEMON_TYPES )
    p1_hp = tf.feature_column.numeric_column("p1_HP")
    p2_hp = tf.feature_column.numeric_column("p2_HP")
    p1_attack = tf.feature_column.numeric_column("p1_Attack")
    p2_attack = tf.feature_column.numeric_column("p2_Attack")
    p1_defense = tf.feature_column.numeric_column("p1_Defense")
    p2_defense = tf.feature_column.numeric_column("p2_Defense")
    p1_special_attack = tf.feature_column.numeric_column("p1_SpAtk")
    p2_special_attack = tf.feature_column.numeric_column("p2_SpAtk")
    p1_special_defense = tf.feature_column.numeric_column("p1_SpDef")
    p2_special_defense = tf.feature_column.numeric_column("p2_SpDef")
    p1_speed = tf.feature_column.numeric_column("p1_Speed")
    p2_speed = tf.feature_column.numeric_column("p2_Speed")

    feature_columns = [pokemon_1, pokemon_2, 
                      p1_type_1, p1_hp, p1_attack, p1_defense, p1_special_attack, p1_special_defense, p1_speed,
                      p2_type_1, p2_hp, p2_attack, p2_defense, p2_special_attack, p2_special_defense, p2_speed]

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
    input_fn=input_fn(data_set=train_data, shuffle=True, batch_size=10000, num_epochs=None),
    steps=20000
  )

  # Use the remaining 20% of data to evaluate accuracy
  eval_results = classifier.evaluate(
    input_fn=input_fn(data_set=test_data, shuffle=False, batch_size=10000, num_epochs=1)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

  # Export SavedModel for upload to the cloud (Google ML engine)
  classifier.export_savedmodel('./export/', json_serving_input_fn)

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)
