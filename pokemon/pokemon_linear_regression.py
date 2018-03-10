import tensorflow as tf
import pokemon_data

def main(argv):

  pokemon_types = [ "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting",
   "Fire","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water" ]

  def build_model_columns():
    # Builds a set of feature columns for the model to use
    pokemon_1 = tf.feature_column.numeric_column('First_pokemon')
    pokemon_2 = tf.feature_column.numeric_column('Second_pokemon')
    pokemon_type_1 = tf.feature_column.categorical_column_with_vocabulary_list('pa_Type', pokemon_types )
    pokemon_type_2 = tf.feature_column.categorical_column_with_vocabulary_list('pb_Type', pokemon_types )
    p1_hp = tf.feature_column.numeric_column("p1_HP")
    p2_hp = tf.feature_column.numeric_column("p2_HP")
    feature_columns = [pokemon_1, pokemon_2, pokemon_type_1, pokemon_type_2, p1_hp, p2_hp]

    return feature_columns

  feature_columns = build_model_columns()

  (train_f, train_l), (test_f, test_l) = pokemon_data.load_data()

  # Build a Linear classifier which chooses between two classes (survived/died)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = feature_columns,
    n_classes = 2)

  classifier.train(
    input_fn = lambda: pokemon_data.input_fn_train(train_f, train_l, 500),
    steps=10000
  )

  eval_results = classifier.evaluate(
    input_fn = lambda: pokemon_data.input_fn_eval(test_f, test_l, 500)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)
