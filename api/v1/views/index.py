#!/usr/bin/python3
"""Returns Status of your API"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify


@app_views.route("/status")
def get_status():
    return jsonify({"status": "OK"})
