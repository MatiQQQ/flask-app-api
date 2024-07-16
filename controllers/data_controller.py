from flask import jsonify


def get_data():
    dummy_data = {"data": "This is some dummy data"}
    return jsonify(dummy_data), 200


def get_info():
    info = {"info": "This is some info"}
    return jsonify(info), 200
