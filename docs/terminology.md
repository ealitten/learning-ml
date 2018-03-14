# Technical documentation for We Predicted That pokemon battle predictor

## Terminology

- **Machine Learning (ML)** - a process by which a machine improves predictions and/or behaviours through the progressive/iterated analysis of large datasets
- **Feature** - A feature is an input variable; the x variable in simple linear regression
- **Label** - A label is the thing we're predicting; the y variable in simple linear regression
- **Model** - A model defines the relationship between features and label, letting us predict the label
- **Training** - Creating or learning the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.
- **Inference** - Applying the trained model to unlabeled examples i.e. using the trained model to make useful predictions (y'). For example, during inference, you can predict the Pokemon battle winner for new unlabelled examples.
- **Training/Test Data** - A supervised ML model needs a labelled dataset to train with, and some further unseen data to evaluate the accuracy of predictions. We therefore split our dataset 80:20 between these two goals; it is important not to use the same data for both as this will not give a true indication of how the model generalises to new data.
- **Linear regression** - Linear regression aims to find a linear relation between a variable (*x*) and an outcome (*y*). If you were to plot this on a graph, the relationship would be *y = mx + c*, where *m* is the slope of our line and *c* is the y-intercept. In machine learning, this is represented as:

  ![we predicted that](https://github.com/ealitten/wepredictedthat/raw/master/docs/images/linear_regression_1_label.png)

  where:

  - *y'* is the predicted label (a desired output)
  - *b* is the bias (the y-intercept)
  - *w* is the weight of a feature (the same concept as the slope on our graph)
  - *x* is a feature (a known input)

  In our model, we are using 16 known inputs, so each one has its own weight:

  ![we predicted that](https://github.com/ealitten/wepredictedthat/raw/master/docs/images/linear_regression_multi_label.png)

  Unfortunately this would require 17 dimensions to represent visually!

- **Logistic regression** - A subcategory of linear regression where the desired output is categorical i.e. it belongs to a number of discrete catgories. In our case just two: pokemon 1 wins or pokemon 2 wins. This makes our problem a *binary classification* problem.