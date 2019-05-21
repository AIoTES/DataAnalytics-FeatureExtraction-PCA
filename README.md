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
The API exposes two methods:<br>
__pca/train__: 
calculates the pca
<br>
__pca/eval__:
evals the pca 
<br>
For further info swagger documentation can be found under << your hosted site >>/docs/ 