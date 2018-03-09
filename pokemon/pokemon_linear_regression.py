import tensorflow as tf
import pokemon_data

def main(argv):

  def build_model_columns():
    # Builds a set of feature columns for the model to use
    pokemon_1 = tf.feature_column.numeric_column('First_pokemon')
    pokemon_2 = tf.feature_column.numeric_column('Second_pokemon')

    feature_columns = [pokemon_1, pokemon_2]

    return feature_columns

  feature_columns = build_model_columns()

  (train_f, train_l), (test_f, test_l) = pokemon_data.load_data()

  # Build a Linear classifier which chooses between two classes (survived/died)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = feature_columns,
    n_classes = 2)

  classifier.train(
    input_fn = lambda: pokemon_data.input_fn_train(train_f, train_l, 50),
    steps=3000
  )

  eval_results = classifier.evaluate(
    input_fn = lambda: pokemon_data.input_fn_eval(test_f, test_l, 50)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)
