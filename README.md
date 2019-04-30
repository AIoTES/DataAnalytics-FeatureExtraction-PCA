# PCA_web_method

This is a Flask based web REST service to use Singular Value Decomposition to provide dimensionality reduction via PCA.
This code implements PCA web service build on top of scikit-learn decompositions method PCA and IncrementalPCA.

## INSTRUCTIONS TO TEST LOCALLY
cd "your working directory"
create a virtual environment via: virtualenv "your_virtual_env_name"
activate virtual env: (linux) source "your_virtual_env_name"/bin/activate (windows) .\"your_virtual_env_name"\Script\activate.bat 
clone repository
run: pip install -r requirements.txt

once all dependecies installed...
__testing:__
this command will run all unit tests
python manage.py test
__launch in localhost:__
this comand will launch the flask resfull API
set enviromental variables (see next section)
python manage.py run

## ENVIRONMENT VARIABLES

__app:__
*API_PROTOCOL*: values: http,https(default)<br>desc:workaround to display swagger documentation in http or https
*WORKING_ENV*:  values:test,dev,prod<br>desc:sets the working environment to test, development or production
*API_HOST*: values: any,0.0.0.0(default)<br>desc: the domain where the API is hosted, by default the host machine
*API_PORT*: values: any available port, 5000(default)<br>desc: the port to expose the API
*LOG_LEVEL*: values:debug,info,warning,error,critical<br>desc: threshold logging level to manage which messages will be showed.
__docker:__
(aquí supongo que se va a usar auto proxy?) Alejandro, por favor ,escribe esta parte y modifica el gitlab ci en consonancia, el docker run está comentado

## USAGE
The API exposes two methods
__pca/train__: 
calculates the pca

__pca/test__:
evals the pca 

For further info swagger documentation can be found under "your host site"/docs/ 