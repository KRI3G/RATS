#!/usr/bin/python3

# This is a barebones auth webhook.
# It lets any user log in with any password
# Not to be used for anything other than testing

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return "Ok"

@app.route("/password", methods=["POST"])
def handle_password():
    data = request.json
    username = data["username"]    

    return jsonify({"success": True, "authenticatedUsername": username})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
