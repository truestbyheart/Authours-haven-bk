#!/usr/bin/python
# coding=utf-8

from flask import Flask, request, jsonify

# init app
app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"status_code": 200, "message": "App is up and running"})

@app.route('/auth/login', methods=['GET'])
login()

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
