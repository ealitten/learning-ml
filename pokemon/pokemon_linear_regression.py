import tensorflow as tf
import pokemon_data

def main(argv):

  # feature_spec = { 'First_pokemon' : tf.FixedLenFeature(50, tf.string),
  #                  'Second_pokemon' : tf.FixedLenFeature(50, tf.string),
  #                   'p1_Type 1' : tf.FixedLenFeature(50, tf.string),
  #                   'p2_Type 1': tf.FixedLenFeature(50, tf.string)
  # }

  # def serving_input_receiver_fn():
  #   # tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec)
  #   serialised_tf_example = tf.placeholder(dtype = tf.string,
  #                                          shape =  50,
  #                                          name = 'input_example_tensor')

  #   receiver_tensors = { 'examples' : serialised_tf_example }
  #   features = tf.parse_example(serialised_tf_example, feature_spec)
  #   return tf.estimator.export.ServingInputReceiver(features, receiver_tensors)

  def json_serving_input_fn():
    """Build the serving inputs."""
    inputs = {}
    for feat in INPUT_COLUMNS:
      inputs[feat.name] = tf.placeholder(shape=[None], dtype=feat.dtype)
      
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)

  def build_model_columns():
    # Builds a set of feature columns for the model to use
    pokemon_1 = tf.feature_column.numeric_column('First_pokemon')
    pokemon_2 = tf.feature_column.numeric_column('Second_pokemon')

    feature_columns = [pokemon_1, pokemon_2]

    return feature_columns

  INPUT_COLUMNS = build_model_columns()

  (train_f, train_l), (test_f, test_l) = pokemon_data.load_data()

  # Build a Linear classifier which chooses between two classes (survived/died)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = INPUT_COLUMNS,
    n_classes = 2)

  classifier.train(
    input_fn = lambda: pokemon_data.input_fn_train(train_f, train_l, 50),
    steps=2000
  )

  eval_results = classifier.evaluate(
    input_fn = lambda: pokemon_data.input_fn_eval(test_f, test_l, 40000)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

  classifier.export_savedmodel('./', json_serving_input_fn)

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)
