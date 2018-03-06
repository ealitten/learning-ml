import tensorflow as tf
import titanic_data

def main(argv):

  def build_model_columns():
    # Builds a set of feature columns for the model to use
    age = tf.feature_column.numeric_column('Age')
    pclass = tf.feature_column.numeric_column('Pclass')
    sex = tf.feature_column.categorical_column_with_vocabulary_list(
      'Sex', ['male', 'female']
    )

    feature_columns = [age, pclass, sex]

    return feature_columns

  feature_columns = build_model_columns()

  (train_f, train_l), (test_f, test_l) = titanic_data.load_data()

  # Build a Linear classifier which chooses between two classes (survived/died)
  classifier = tf.estimator.LinearClassifier(
    feature_columns = feature_columns,
    n_classes = 2)

  classifier.train(
    input_fn = lambda: titanic_data.input_fn_train(train_f, train_l, 50),
    steps=2000
  )

  eval_results = classifier.evaluate(
    input_fn = lambda: titanic_data.input_fn_eval(test_f, test_l, 50)
  )

  print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))

if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)