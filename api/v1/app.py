#!/usr/bin/python3
"""script that intializes app.py"""

from flask import Flask
from models import storage
from os import getenv
from flask import make_response, jsonify
from api.v1.views import app_views
from flask import Blueprint

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(self):
    """function that closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')),
            threaded=True)
