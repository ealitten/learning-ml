# We Predicted That

Welcome to We Predicted That's machine learning excellence!

## Introduction

This repo details We Predicted That's "final week" machine learning project from the December 2017 Makers Academy cohort.

Our team is:

 - [Reena  Sharma](https://github.com/reenz)
 - [Ed Litten](https://github.com/ealitten)
 - [Tom Grand](https://github.com/Tagrand)
 - [Ed Goold](https://github.com/Gleoman)
 - [Dom Vernon](https://github.com/domvernon)

## Installation/Requirements

- tensorflow
- pandas

All requirements can be installed by installing the pipenv library (`pip install pipenv`) and then running `pipenv install` in the project directory. This will create a virtual environment with the dependencies installed - to run commands in the environment first run `pipenv shell`.


## Project Description

We defined our initial project aim as: 
```Making predictions using machine learning```

Since we were all new to machine learning and data science, we started the project with a mini learning project: [predicting who survives the sinking of the Titanic](https://www.kaggle.com/c/titanic). This is a popular starting project for ML, and is a good introduction to the simpler ML algorithms. The challenge is a relatively straightforward binary classification problem - there are two outcomes: survived and died. We solved this using a logistic regression algorithm, using three columns from the Titanic dataset (`age`, `sex` and `passenger class`), achieving 80-82% accuracy of prediction. The titanic model and data can be found in the `titanic` folder.

Once we had solved the titanic challenge, we chose a main project: using a dataset of pokemon attributes and battles to predict the winner in a battle between any two Pokemon. The [dataset](https://www.kaggle.com/terminus7/pokemon-challenge) was obtained from kaggle.


## MVP

We defined our learning project MVP as:
```Using Titanic survivor data, predict the survival outcome of passengers a better than chance.```

The MVP for our main project was defined as:
```Using the historical battle data and Pokemon attributes, predict the outcome of a battle with accuracy over 75%```

## Features implemented

- Pokemon model can predict the outcome of the battle with ~52% accuracy, using two feature columns (player 1, player 2)


## Technologies Used

 - Python
 - [TensorFlow](https://www.tensorflow.org) - Machine learning library
 - [Pandas](https://pandas.pydata.org) - Data structure library


## Terminology

 - _Machine Learning_ - a process by which a machine improves predictions and/or behaviours through the progressive/iterated analysis of large datasets
 - _Feature_ - A feature is an input variable; the x variable in simple linear regression
 - _Label_ - A label is the thing we're predicting; the y variable in simple linear regression
 - _Model_ - A model defines the relationship between features and label, letting us predict the label
 - _Training_ - Creating or learning the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.
- _Inference_ - Applying the trained model to unlabeled examples i.e. using the trained model to make useful predictions (y'). For example, during inference, you can predict the Pokemon battle winner for new unlabelled examples.
 - _Test/Training Data_ - 
