![we predicted that](https://github.com/ealitten/wepredictedthat/raw/master/docs/images/wp_blue_200.png)

# We Predicted That

Welcome to We Predicted That's machine learning excellence!

## Introduction

This repo details We Predicted That's "final week" machine learning project from the December 2017 Makers Academy cohort.

Our team:

- [Reena  Sharma](https://github.com/reenz)
- [Ed Litten](https://github.com/ealitten)
- [Tom Grand](https://github.com/Tagrand)
- [Ed Goold](https://github.com/Gleoman)
- [Dom Vernon](https://github.com/domvernon)


## Project Description

We defined our initial project aim as: 
```
Making predictions using machine learning
```

Since we were all new to machine learning and data science, we started the project with a mini learning project: [predicting who survives the sinking of the Titanic](https://www.kaggle.com/c/titanic). This is a popular starting project for ML, and is a good introduction to the simpler ML algorithms. The challenge is a relatively straightforward binary classification problem - there are two outcomes: survived and died. We solved this using a logistic regression algorithm, using three columns from the Titanic dataset (`age`, `sex` and `passenger class`), achieving 80-82% accuracy of prediction. The titanic model and data can be found in the `titanic` folder.

Once we had solved the titanic challenge, we chose a main project: using a dataset of pokemon attributes and battles to predict the winner in a battle between any two Pokemon. The [dataset](https://www.kaggle.com/terminus7/pokemon-challenge) was obtained from kaggle.


## Approach

1. See our [documentation file](https://github.com/ealitten/we-predicted-that/blob/master/ml-models/pokemon/documentation.md) for more detail on the technical implementation
2. Have a look at our [team blog](https://medium.com/@wepredictedthat) for the teamwork side of things


## MVP

We defined our learning project MVP as:
```
Using Titanic survivor data, predict the survival outcome of passengers a better than chance.
```

The MVP for our main project was defined as:
```
Using the historical battle data and Pokemon attributes, predict the outcome of a battle with accuracy over 75%
```


## Features implemented

- A pokemon battle model which predicts the outcome of a fight between two pokemon
  - Logistic regression method used for prediction
  - Accuracy of ~87%
  - Trained on a dataset of 40,000 outcomes, using 16 feature columns
  - Model hosted on Google ML engine for online prediction requests

- A web app which provides an interface for the prediction model
  - The user can select two pokemon to fight and see the predicted outcome
  - The user can see images of the pokemon, and see their stats before the battle

## Technologies Used

- Python
- [TensorFlow](https://www.tensorflow.org) - Machine learning library
- [Pandas](https://pandas.pydata.org) - Data structure library
- [Django](https://www.djangoproject.com/) - Python web framework
- [Google ML engine](https://cloud.google.com/ml-engine/) - Managed service to host custom machine learning model


## Installation/Requirements

- python 3.6

All required packages can be installed by installing the pipenv library (`pip install pipenv`) and then running `pipenv install` in the project directory. This will create a virtual environment with the dependencies installed - to run commands in the environment first run `pipenv shell`. By default, pipenv will only install production packages (required for the Django website) - to install packages required to build the tensorflow model, use `pipenv install --dev`.

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
