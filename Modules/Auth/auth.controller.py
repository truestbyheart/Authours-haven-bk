from flask import request, jsonify


def login():
    if request.method == 'GET':
        print('Endpoint hit')
        return jsonify({"status": 200})
