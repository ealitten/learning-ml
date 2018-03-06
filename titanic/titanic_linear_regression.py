import tensorflow as tf

def build_model_columns():
  # Builds a set of feature columns for the model to use
  age = tf.feature_column.numeric_column('age')
  pclass = tf.feature_column.numeric_column('pclass')
  sex = tf.feature_column.categorical_column_with_vocabulary_list(
    'sex', ['male', 'female']
  )

  feature_columns = [age, pclass, sex]

  return feature_columns

def input_fn():
  # Generate an input function for the estimator
  dataset = []
  return dataset


def main():

  feature_columns = build_model_columns()

  # Build a Linear classifier which chooses between two classes (survived/died)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = feature_columns,
    n_classes = 2)

  classifier.train(
    input_fn = lambda: input_fn()
  )

  eval_results = classifier.evaluate(
    input_fn = lambda: input_fn()
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))