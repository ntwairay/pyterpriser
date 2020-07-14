# Terraform Enterprise api #
This python api is to execute a script on the localhost to create stitching video

## Components ##
- Python
- Flask
- Flask Restful
- Gunicorn
- Virtualenv (for local development)

### Running on local ###
- python3 -m venv env
- . env/bin/activate
- pip3 install -r requirements.txt
- ./src/api.py

### Running on docker container with mounting docker.sock and volumes ###
- docker run -p 5000:5000 -ti -v /var/run/docker.sock:/var/run/docker.sock -v MY_VOLUME/join.sh:/tmp/scripts/join.sh --env SCRIPT_PATH=/tmp/scripts/join.sh police/pyapi:latest

### Testing the API ###

#### Creating stitch video ####
***curl -X POST http://0.0.0.0:5000/createstitch***
