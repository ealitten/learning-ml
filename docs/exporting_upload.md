# Technical documentation for We Predicted That pokemon battle predictor

## Step 3 - Exporting & uploading the model

Once our model was trained to our satisfaction, and could produce reasonable results, the next step was to export it so that we could upload it to the Google ML engine platform. This lets us send it prediction requests remotely! Fortunately Google supports uploading saved tensorflow models in the 'SavedModel' format, and tensorflow has a function to export as a savedmodel.

A few code changes are required for the model to handle online requests. Firstly, it needs a serving input function - this is similar to the training/evaluation input function used to transform data into tensors, but needs to be written for the specific input type. It returns a ServingInputReceiver object, which contains placeholders for the incoming data. Since we only planned to send the model requests in JSON format, we simply added a json serving input function as documented in the tensorflow documentation:

```python
  def json_serving_input_fn():
    """Builds serving input fn which is used when model is running in cloud"""
    inputs = {}
    for feat in INPUT_COLUMNS:
      inputs[feat.name] = tf.placeholder(shape=[None], dtype=feat.dtype)
      
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)
```

The basic steps to export & upload the model to ML engine are as follows (assuming you have the GCloud sdk installed and are authenticated):

1. Add code to py file to export the saved model once training is finished:

```
classifier.export_savedmodel('./export/', json_serving_input_fn)
```

  This takes the serving input function as one of its arguments.

2. Copy the resulting saved model folder to a Google storage bucket

3. Create version of model from the saved model folder:

```
gcloud ml-engine models versions create v10 —model pokemon_predictor --origin gs://wepredictedthat-pokemon/export/15208652 --runtime-version 1.4
```

4. Sending a test query to the ML engine
```
gcloud ml-engine predict --model pokemon_predictor --version v10 --json-instances test_query.json
```

Unfortunately, for our team these steps took several days of painful experimentation to get working! It turns out that tensorflow is very sensitive to different versions - we produced our saved model in TF 1.6 (the current version), but ML engine only runs version 1.4. Attempting to upload a model produced in v1.6 produced some very cryptic errors which are not particularly easy to look up.

```
{
  "error": "Prediction failed: Error during model execution: AbortionError(code=StatusCode.INVALID_ARGUMENT, details=\"NodeDef mentions attr 'output_type' not in Op<name=ArgMax; signature=input:T, dimension:Tidx -> output:int64; attr=T:type,allowed=[DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT32, DT_UINT8, DT_UINT16, DT_INT16, DT_INT8, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8, DT_QUINT8, DT_QINT32, DT_HALF]; attr=Tidx:type,default=DT_INT32,allowed=[DT_INT32, DT_INT64]>; NodeDef: linear/head/predictions/class_ids = ArgMax[T=DT_FLOAT, Tidx=DT_INT32, _output_shapes=[[-1]], output_type=DT_INT64, _device=\"/job:localhost/replica:0/task:0/cpu:0\"](linear/head/predictions/two_class_logits, linear/head/predictions/class_ids/dimension)\n\t [[Node: linear/head/predictions/class_ids = ArgMax[T=DT_FLOAT, Tidx=DT_INT32, _output_shapes=[[-1]], output_type=DT_INT64, _device=\"/job:localhost/replica:0/task:0/cpu:0\"](linear/head/predictions/two_class_logits, linear/head/predictions/class_ids/dimension)]]\")"
}
```

Re-producing and exporting the model in TF 1.4 required significant refactoring of the code, as our original code took advantage of several functions only introduced in later versions. A second pain point was that it's critically important to specify the runtime version (in step 3 above) when creating a new version of the model - if you do this via the UI on the Google ML engine website there is no option to specify this, and if you don't specify the runtime matching your saved model it won't work!

Once you sucessfully send a request to the model, it will send a response with the predicted class and the % confidence for each class, e.g.

```
[{'probabilities': [0.9882336854934692, 0.01176633220165968], 'logits': [-4.4306769371032715], 'classes': ['0'], 'class_ids': [0], 'logistic': [0.01176633220165968]}]
```

This translates to the Winner being class 0 (i.e. pokemon 1 wins) with 98.8% confidence.