#!/usr/bin/python3

# This is the config webhook
# It is used by the container
# backend after the user has
# authenticated to configure
# user specific container settings

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return "Ok"

@app.route("/", methods=["POST"])
def handle_json_request():
    data = request.json
    authenticated_username = data.get('authenticatedUsername')
    
    # Check if the user home folder exists, otherwise create it
    folder_path = os.path.join('/users/', authenticated_username)
    if not os.path.exists(folder_path):
        os.umask(0o000)
        os.makedirs(folder_path, mode=0o777, exist_ok=True)
        os.umask(0o022)
        print(f"[CONFIG] Creating home directory for {authenticated_username}")
    folder_path = os.path.abspath(folder_path)

    return jsonify({"config": {"docker": {"execution": {"host": {"binds": [f"{folder_path}:/home/user:z"]}}}}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
