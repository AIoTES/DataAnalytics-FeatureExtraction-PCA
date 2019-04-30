# PCA_web_method

This is a Flask based web REST service to use Singular Value Decomposition to provide dimensionality reduction via PCA.
This code implements PCA web service build on top of scikit-learn decompositions method PCA and IncrementalPCA.

swagger documentation can be found under "your host site"/docs/ 

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
API_PROTOCOL: values: http,https(default) desc:workaround to display swagger documentation in http or https
__docker:__
(aquí supongo que se va a usar auto docker?)

