# Technical documentation for We Predicted That pokemon battle predictor

## Step 2 - Writing and training the model

In machine learning, there are two types of algorithm: supervised and unsupervised. Supervised  learning is when you provide the algorithm with the 'right' answers (the label) -  e.g. you wanted a machine to learn to choose between cats and dogs, you'd give it a dataset of cat & dog photos, with labels identifying which class ("cat" or "dog") each photo belonged to. As the training function runs through the data, it builds a model using this training data. 

### Loss functions
As it trains, the model makes a prediction and then compares this to the label given to that row of the data set - it measures the overall accuracy of its predictions with a 'loss function'. Loss is the penalty for a bad prediction i.e. , loss is a number indicating how bad the model's prediction was on a single example. he goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples. In Linear Regression this is often done using the mean square error: it takes the numerical differences between the predicted value and the label, then squares each of these and takes the mean across the data set. Squaring the values penalises far-off predictions more heavily than close ones, so the function favours several close results over one perfect prediction and one far-off one.

### The balance of training
When you train a machine, its all about trying to balance the accuracy with getting quick results and the computing power you have to hand (our data is small, so there was relatively little issues with the third). When you try and improve your model you essentially have four factors to control how good it is/how fast it runs. 

1. **Steps** - the more steps, the more likely it will be to get close to finishing near the optimal point. 
2. **Batch size** - the bigger the batch size (the highest being the actual size of your dataset). If you feed the whole data set in before it evaluates, the model will improve much more gradually but is more likely to end up with a better accuracy. Because it has larger chunks of data, its predictions will vary less wildly, so its progression towards the optimal result will be more smooth. Sets that are too small can vary so wildly, that the model can jump from being OK to being terrible, and then back to terrible again. 
3) **More variables** - in our case we can add more stats about pokemon. Again this slows it down, and also is annoying for predictions as we need more stats to feed in. 
4) **Algorithm type** - different algorithms have their strengths and weaknesses. So they can change speed, accuracy. We stuck with logistic regression for Tensorflow and that reached 86% accuracy, but given more time we would have liked to extend this to combine with a neural network (known as a "wide and deep" model). During testing with a random forest algorithm in a different ML library (SciKit Learn) we achieved 94.1% accuracy.  

We have a relatively small data set, so our computers could run a full batch size happily (albeit slowly) when we trained the data. However, it couldn't be too slow or we couldn't try out all combinations of pokemon stats, so we attempted to find out which variables had the greatest effect on accuracy.

For example, small batch sizes (500) with lower numbers of steps (1000) took a mere minute to run, but when we starting adding 18 different stats for the pokemon, running with batch sizes of (10,000) for (20,000) steps, it took over an hour to train.

We found that a good approach is to first start with smaller batch sizes and steps. Start testing to see if adding more variables are making a difference. Then we started increasing the number of steps, and you could generally spot when steps started to have minimal impact (as the loss function stops decreasing). Then, if that particular set looked good, increase the batch size and go for lunch. 

The graph below shows our progress:


Eventually, following this cycle we found a good set of stats, using 18 variables (excluding Pokemon name and generation) and ran it at a batch size of 10,000, with 20,000 steps and reached 86.1% accuracy.
