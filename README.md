# PCA_web_method

This is a Flask based web REST service to use Singular Value Decomposition to provide dimensionality reduction via PCA.<br>
This code implements PCA web service build on top of scikit-learn decompositions method PCA and IncrementalPCA.<br>

## INSTRUCTIONS TO TEST LOCALLY
1. cd "your working directory"<br>
1. create a virtual environment via: `virtualenv "your_virtual_env_name"`<br>
1. activate virtual env: (linux) `source "your_virtual_env_name"/bin/activate` (windows) `.\"your_virtual_env_name"\Script\activate.bat`<br> 
1. clone repository<br>
1. run: `pip install -r requirements.txt`<br>

once all dependecies installed...

__testing:__
this command will run all unit tests

`python manage.py test`

__launch in localhost:__
this comand will launch the flask resfull API, remember set enviromental variables (see next section)

`python manage.py run`

### DEPLOY ON DOCKER
1. clone this repository
2. open a shell
3. cd to the directory where the repository has been downloaded
4. build the image:  `docker build -t <<image_name>> .`
5. run the image with the desired environmental variables (see next section): Ex.`docker run --env=”API_PORT=8000” --env"API_PROTOCOL=http" -p 8000:8000 <<image_name>>:latest`

## ENVIRONMENT VARIABLES
 - *API_PROTOCOL*: 
    - values: http,https(default)
    - desc:workaround to display swagger documentation in http or https<br>
 - *WORKING_ENV*:  
    - values:test,dev,prod
    - desc:sets the working environment to test, development or production<br>
 - *API_HOST*: 
    - values: any,0.0.0.0(default)
    - desc: the domain where the API is hosted, by default the host machine<br>
 - *API_PORT*: 
    - values: any available port, 5000(default)
    - desc: the port to expose the API
 - *LOG_LEVEL*: 
    - values:debug,info,warning,error,critical
    - desc: threshold logging level to manage which messages will be showed<br>


## USAGE
The API exposes two methods explained below

For further info swagger documentation can be found under https://localhost:5000/docs/ (when using the default environment variables and running locally, update URL accordingly). 

### pca/train
POST method
calculates the pca, given the methodology:
- options:
    - pca: classic pca method applying a previous standard scaler to data provided.
    - pca_raw: classic pca method without applying a previous standard scaler.
    - ipca: incremental pca method applying a previous standard scaler to use with large datasets.(batch_size must be specified)
    - ipca_raw: incremental pca method without applying a previous standard scaler.(batch _size must be specified)
- query: please check app/main/model/connect_db.py to complete the datat link
- raw_data: json serialized input stream format:{"columns":[],"index":[],"data":[[]]}
- n_components: number of components desired

*Example of test call:*
note that query:"test" just loads the infamous [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) to emulate the query
```
{
  "dataDesc": {
    "query": "test" 
  },
  "options": "pca",
  "n_components":3
}
```
will return:
```
{
  "status": "ok",
  "components": [
    [
      0.5210659146701195,
      -0.26934744250594367,
      0.5804130957962945,
      0.5648565357793612
    ],
    [
      0.3774176155645673,
      0.9232956595407151,
      0.024491609085586785,
      0.06694198696805842
    ],
    [
      -0.7195663527008169,
      0.2443817795143992,
      0.1421263693339043,
      0.6342727371109227
    ]
  ],
  "explained_variance": [
    2.9380850501999953,
    0.9201649041624886,
    0.14774182104494812
  ],
  "explained_variance_ratio": [
    0.7296244541329985,
    0.2285076178670179,
    0.036689218892828765
  ],
  "singular values": [
    20.923065561236463,
    11.709166098412423,
    4.6918579833257175
  ],
  "n_components": 3,
  "noise_variance": 0.020853862176462328,
  "model_stream": "gANC5wUAAIADY3NrbGVhcm4ucGlwZWxpbmUKUGlwZWxpbmUKcQApgXEBfXECKFgFAAAAc3RlcHNx\nA11xBChYBgAAAHNjYWxlcnEFY3NrbGVhcm4ucHJlcHJvY2Vzc2luZy5kYXRhClN0YW5kYXJkU2Nh\nbGVyCnEGKYFxB31xCChYCQAAAHdpdGhfbWVhbnEJiFgIAAAAd2l0aF9zdGRxCohYBAAAAGNvcHlx\nC4hYDwAAAG5fc2FtcGxlc19zZWVuX3EMY251bXB5LmNvcmUubXVsdGlhcnJheQpzY2FsYXIKcQ1j\nbnVtcHkKZHR5cGUKcQ5YAgAAAGk4cQ9LAEsBh3EQUnERKEsDWAEAAAA8cRJOTk5K/////0r/////\nSwB0cRNiQwiWAAAAAAAAAHEUhnEVUnEWWAUAAABtZWFuX3EXY251bXB5LmNvcmUubXVsdGlhcnJh\neQpfcmVjb25zdHJ1Y3QKcRhjbnVtcHkKbmRhcnJheQpxGUsAhXEaQwFicRuHcRxScR0oSwFLBIVx\nHmgOWAIAAABmOHEfSwBLAYdxIFJxIShLA2gSTk5OSv////9K/////0sAdHEiYolDIGEs+cWSXxdA\nRBm9LWt1CECw8dJNYhAOQJq1OiZ4MPM/cSN0cSRiWAQAAAB2YXJfcSVoGGgZSwCFcSZoG4dxJ1Jx\nKChLAUsEhXEpaCGJQyDIvqDUwMvlP0hEDnO+J8g/7hzw5pbDCEAzKWdk33fiP3EqdHErYlgGAAAA\nc2NhbGVfcSxoGGgZSwCFcS1oG4dxLlJxLyhLAUsEhXEwaCGJQyAbCjJB3mjqP3Sm3Khjzds/D0Wv\n4IQm/D8sRPvpZk/oP3ExdHEyYlgQAAAAX3NrbGVhcm5fdmVyc2lvbnEzWAYAAAAwLjIwLjNxNHVi\nhnE1WAMAAABwY2FxNmNza2xlYXJuLmRlY29tcG9zaXRpb24ucGNhClBDQQpxNymBcTh9cTkoWAwA\nAABuX2NvbXBvbmVudHNxOksDaAuIWAYAAAB3aGl0ZW5xO4lYCgAAAHN2ZF9zb2x2ZXJxPFgEAAAA\nYXV0b3E9WAMAAAB0b2xxPkcAAAAAAAAAAFgOAAAAaXRlcmF0ZWRfcG93ZXJxP2g9WAwAAAByYW5k\nb21fc3RhdGVxQE5YDwAAAF9maXRfc3ZkX3NvbHZlcnFBWAQAAABmdWxscUJoF2gYaBlLAIVxQ2gb\nh3FEUnFFKEsBSwSFcUZoIYlDIDMzMzMzc968mpmZmZmZ4LyamZmZmZnevGPJL5b8Ytm8cUd0cUhi\nWA8AAABub2lzZV92YXJpYW5jZV9xSWgNaCFDCNs7LAC3WpU/cUqGcUtScUxYCgAAAG5fc2FtcGxl\nc19xTUuWWAsAAABuX2ZlYXR1cmVzX3FOSwRYCwAAAGNvbXBvbmVudHNfcU9oGGgZSwCFcVBoG4dx\nUVJxUihLAUsDSwSGcVNoIYlDYBIx0mySrOA/0MA0Dv080b+4rxN8vpLiP7FVgwNOE+I/+i7yNpwn\n2D8ShMhWo4vtPyAwMhBUFJk/SM/BLBwjsT9E3QQEsAbnvxhWYPPmR88/ZxsYZjIxwj+gWNRW9kvk\nP3FUdHFVYlgNAAAAbl9jb21wb25lbnRzX3FWSwNYEwAAAGV4cGxhaW5lZF92YXJpYW5jZV9xV2gY\naBlLAIVxWGgbh3FZUnFaKEsBSwOFcVtoIYlDGNLNG7wygQdAcMFJq/1x7T9X3NE4NOnCP3FcdHFd\nYlgZAAAAZXhwbGFpbmVkX3ZhcmlhbmNlX3JhdGlvX3FeaBhoGUsAhXFfaBuHcWBScWEoSwFLA4Vx\nYmghiUMYW54bYhVZ5z8sF9DUvD/NP0ZehebtyKI/cWN0cWRiWBAAAABzaW5ndWxhcl92YWx1ZXNf\ncWVoGGgZSwCFcWZoG4dxZ1JxaChLAUsDhXFpaCGJQxgSk00GTuw0QP85oNEXaydAH3FPa3bEEkBx\nanRxa2JoM2g0dWKGcWxlWAYAAABtZW1vcnlxbU5oM2g0dWIucQAu\n"
}
```

Please refer to [scikit learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) for a deeper understanding of each returned element.
Additionaly, "model_stream" returns the serialised model to be used in calls to the pca/eval method. 

### pca/eval
evals the pca 
- "dataDesc": follows the input from previous method
- "n_components": sets the number of components to be returned (it can be equal or less to the components provided by the pca model
- "raw_model": model serialised returned by "model _stream"