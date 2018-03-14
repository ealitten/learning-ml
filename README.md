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

Details on the technical implementation:

1. [Intro to Machine Learning & terminology](https://github.com/ealitten/we-predicted-that/blob/master/docs/terminology.md))
2. [Data munging](https://github.com/ealitten/we-predicted-that/blob/master/docs/data_munging.md)
3. [Training the model](https://github.com/ealitten/we-predicted-that/blob/master/docs/training.md) (WIP)
4. [Exporting and uploading the model to Google ML engine](https://github.com/ealitten/we-predicted-that/blob/master/docs/exporting_upload.md)
5. [Building a web app in Django](https://github.com/ealitten/we-predicted-that/blob/master/docs/django.md) (WIP)
6. [Linking up the web app on Heroku with the model](https://github.com/ealitten/we-predicted-that/blob/master/docs/heroku_ml_engine.md)

Have a look at our [team blog](https://medium.com/@wepredictedthat) for the teamwork side of things!




## MVP

We defined our learning project MVP as:
```
Using Titanic survivor data, predict the survival outcome of passengers a better than chance.
```

The MVP for our main project was defined as:
```
Using the battle data and Pokemon attributes, predict the outcome of a battle with accuracy >75%
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

## Technologies / plaforms used

- Python
- [TensorFlow](https://www.tensorflow.org) - Machine learning library
- [Pandas](https://pandas.pydata.org) - Data structure library
- [Django](https://www.djangoproject.com/) - Python web framework
- [Google ML engine](https://cloud.google.com/ml-engine/) - Managed service to host custom machine learning model
- [Heroku](https://www.heroku.com/) - Platform to deply our Django web app


## Installation/Requirements

- python 3.6

All required packages can be installed by installing the pipenv library (`pip install pipenv`) and then running `pipenv install` in the project directory. This will create a virtual environment with the dependencies installed - to run commands in the environment first run `pipenv shell`. By default, pipenv will only install production packages (required for the Django website) - to install packages required to build the tensorflow model, use `pipenv install --dev`.
