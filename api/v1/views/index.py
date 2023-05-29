#!/usr/bin/python3
"""Returns Status of your API"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route("/status", methods=['GET'])
def status():
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    new_dict = {}
    for keys, values in classes.items():
        new_dict[keys] = storage.count(values)
    return jsonify(new_dict)
