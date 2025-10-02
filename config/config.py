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
    # folder_path = os.path.join('/users/', authenticated_username)
    # if not os.path.exists(folder_path):
    #     os.umask(0o000)
    #     os.makedirs(folder_path, mode=0o777, exist_ok=True)
    #     os.umask(0o022)
    #     print(f"[CONFIG] Creating home directory for {authenticated_username}")
    # folder_path = os.path.abspath(folder_path)

    # This depends on where your RATS is installed
    return jsonify({
        "config": {
            "docker": {
                "execution": {
                    "host": {
                        "binds": [
                            f"/opt/RATS/users/{authenticated_username}:/home/{authenticated_username}:z"
                        ]
                    }, 
                    "container": {
                        #"cmd": [
                        #    f"/usr/sbin/useradd {authenticated_username} -s /bin/bash && && /usr/bin/su - {authenticated_username} && exit"
                        #]
                        #"user": "student"
                    }
                    #"idleCommand": [
                    #    "/sbin/init"
                    #],
                    #"shellCommand": [
                    #    "/sbin/init"
                    #]
                    #"idleCommand": [
                    #    "/bin/sh", "-c", f"/usr/sbin/useradd {authenticated_username} -s /bin/bash && /usr/bin/su - {authenticated_username}"
                    #],
                    #"shellCommand": [
                    #    "/bin/sh", "-c", f"/usr/sbin/useradd {authenticated_username} -s /bin/bash && /usr/bin/su - {authenticated_username}"
                    #]
                }
            }
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
