# Technical documentation for We Predicted That pokemon battle predictor

## Step 2 - Writing and training the model

In machine learning, there are two types of algorithm. Supervised and Unsupervised. 
We just used supervised machine learning, but if you want to learn more about unsupervised have a look here[]. 

Supervised is when you provide the algorithm with the 'right' answers. So say you wanted a machine to learn to choose between cats and dogs, you'd give it a tonne of photos of cats and dogs, with labels saying, if they were cats and dogs. You feed them all into the machine (after some data munging and tidying) and the machine tries to spot patterns. In our case, we gave it a tonne of battles between pokemon with the results. 

As it runs through the data, it builds a model (following the rules of the algorithm, there are lots of different ones for different scenarios, and each have different possitives and negatives) using this training data.

Once its done this, it then *Tests* the model with a new set of data. Again these have the 'answers' or labels attached to them, and the model then sees how close it is with each of its predictions. It then, measures this accuracy with a 'loss function'. To cut a long story short, the loss function is measuring not just how good its predictions were, but how varied they are. The machine would rather have a lot of mediocre results which were slightly off, then sometimes be totally right, and other times be wildly off. It values predictability highly. It then loops round and tries again and again. How many times it loops round is called **Steps**, the size of the data set it feeds in before it evaluates is called the **batch size**.

When you train a machine, its all about trying to balance the accuracy, with getting quick results and the computing power you have (our data is small, so there was relatively little issues with the third). When you try and improve your model you essentially have four factors to control how good it is/how fast it runs. 

1) Steps - the more steps, the more likely it will be to get close to finishing near the optimal point. 
2) Batch size - the bigger the batch size (the highest being the actual size of your dataset, so you feed the whole data set in before it evaluates) the slower your machine will improve at first as its got tonnes more information, but it will improve much more gradually. Because its got larger chunks of data, its predictions will vary less wildly. So its progression towards the optimal result will be more smooth. Sets that are too small can vary so wildly, that the model can jump from being OK to being terrible, and then back to terrible again. 
3) More variables (Sometimes) in our case we can add more stats about pokemon. Again this slows it down, and also is annoying for predictions as we need more stats to feed in. 
4) Algorithm type - different algorithms have their strengths and weaknesses. So they can change speed, accuracy. We stuck with linear regression for Tensorflow and that reached 86% accuracy. But with a random tree algorithm we achieved 94.1% accuracy.  

For us, we have a relatively small data set, so our computers could run a full batch size happily (ableit slowly) when we trained the data. But it couldn't be too slow, or we couldn't try out all combinations of pokemon stats, so it slowed progress to find which variables mattered (you could bung all of them in, but this seems lazy and we wanted to see which stats actually seemed to matter!)

For example, small batch sizes (500) with lower numbers of steps (1000) took a mere minute to run, but when we starting adding 18 different stats for the pokemon, running with batch sizes of (10,000) for (20,000) steps. It took an hour! 

So a good cycle is to first start with smaller batch sizes and steps. Start testing to see if adding more variables are making a difference. Then we started increasing the number of steps, and you could generally spot when steps started to have minimal impact (as the loss function stops decreasing). Then, if that particular set looked good, increase the batch size and go for lunch. 

The graph below shows our progress. 


Eventually following this cycle, we found a good set of stats, using 18 variables (but excluding name and generation) and ran it at a batch size of 10,000, with 20,000 steps and reached 86.1% accuracy. We also used a random tree algorithm, which returned a 94.1% accuracy level. And even ranked which options were the best:



Further reading:






