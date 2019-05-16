# PCA_web_method

This is a Flask based web REST service to use Singular Value Decomposition to provide dimensionality reduction via PCA.<br>
This code implements PCA web service build on top of scikit-learn decompositions method PCA and IncrementalPCA.<br>

## INSTRUCTIONS TO TEST LOCALLY
cd "your working directory"<br>
create a virtual environment via: `virtualenv "your_virtual_env_name"`<br>
activate virtual env: (linux) `source "your_virtual_env_name"/bin/activate` (windows) `.\"your_virtual_env_name"\Script\activate.bat`<br> 
clone repository<br>
run: `pip install -r requirements.txt`<br>
<br>
once all dependecies installed...<br>
__testing:__<br>
this command will run all unit tests<br>
`python manage.py test`<br>
__launch in localhost:__<br>
this comand will launch the flask resfull API<br>
set enviromental variables (see next section)<br>
`python manage.py run`<br>

### DEPLOY ON DOCKER
1. clone this repository
2. open a shell
3. cd to the directory where the repository has been downloaded
4. build the image:  `docker build -t <<image_name>> .`
5. run the image with the desired environmental variables (see next section): Ex.`docker run --env=”API_PORT=8000” -p 8000:8000 -e <<image_name>>:latest`

## ENVIRONMENT VARIABLES

__app:__<br>
*API_PROTOCOL*: values: http,https(default)<br>desc:workaround to display swagger documentation in http or https<br>
*WORKING_ENV*:  values:test,dev,prod<br>desc:sets the working environment to test, development or production<br>
*API_HOST*: values: any,0.0.0.0(default)<br>desc: the domain where the API is hosted, by default the host machine<br>
*API_PORT*: values: any available port, 5000(default)<br>desc: the port to expose the API<br>
*LOG_LEVEL*: values:debug,info,warning,error,critical<br>desc: threshold logging level to manage which messages will be showed<br>
__docker:__<br>
    *$DOCKER_USER*: DockerID or user of your service registry.
    *$DOCKER_PASSOWORD*: Password to access your registry.
    *$DOCKER_SERVER*: IP or DNS of you registry.
    *$IMAGE_NAME*: Name provided to your built image.
    *$CI_COMMIT_REF_SLUG*: reference label provided to your image (e.g. latest). 


## USAGE
The API exposes two methods:<br>
__pca/train__: 
calculates the pca
<br>
__pca/test__:
evals the pca 
<br>
For further info swagger documentation can be found under << your hosted site >>/docs/ 