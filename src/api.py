#! /usr/bin/env python
import os
import subprocess
import pyterprise
from flask import Flask, jsonify, request
from flask_cors import CORS
from subprocess import run
from subprocess import Popen, PIPE
from subprocess import check_output

tfe_token = ""
aws_access_key_id = ""
aws_secret_access_key = ""
client = pyterprise.Client()

# Supply your token as a parameter and the url for the terraform enterprise server.
# If you are not self hosting, use the one provided by hashicorp.
client.init(token=tfe_token, url='https://ptfe.servian-sg.gradeous.io')

def create_workspace(payload):
    vcs_options = {
        "identifier": "ntwairay/rich-value-type-test",
        "oauth-token-id": "ot-wfuy8qmxZV8oEpvW",
        "branch": "master",
        "default-branch": False
    }
    org = client.set_organization(id=payload['id'])
    org.create_workspace(name=payload['name'],
                         vcs_repo=vcs_options,
                         auto_apply=False,
                         queue_all_runs=False,
                         working_directory='/',
                         trigger_prefixes=['/'])
    workspace = org.get_workspace(payload['name'])
    workspace.create_variable(key='AWS_ACCESS_KEY_ID', value=aws_access_key_id, sensitive=True, category='terraform')
    workspace.create_variable(key='AWS_SECRET_ACCESS_KEY', value=aws_secret_access_key, sensitive=True, category='terraform')
    return "<h3> Onboarding is completed <h3>"

def create_plan(payload):
    org = client.set_organization(id=payload['id'])
    workspace = org.get_workspace(payload['name'])
    workspace.plan_apply(destroy_flag=False,message="run from api")
    return "<h3> Plan and apply are completed <h3>"

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h3> You are using PTFE API <h3>"

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/createworkspace', methods=['POST'])
def createworkspace():
    payload = request.get_json()
    return create_workspace(payload)

@app.route('/createplan', methods=['POST'])
def createwplan():
    payload = request.get_json()
    return create_plan(payload)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
