# Technical documentation for We Predicted That pokemon battle predictor

## Step 3 - Exporting & uploading the model

1. Add code to py file to export the saved model once training is finished:

```
classifier.export_savedmodel('./export/', json_serving_input_fn)
```

2. Copy saved model folder (e.g. 15208652) to google storage bucket

3. Create version of model from the saved model folder

```
gcloud ml-engine models versions create v10 —model pokemon_predictor --origin gs://wepredictedthat-pokemon/export/15208652 --runtime-version 1.4
```

4. Sending a test query to the ML engine
  ```
  gcloud ml-engine predict --model pokemon_predictor --version v10 --json-instances test_query.json
  ```