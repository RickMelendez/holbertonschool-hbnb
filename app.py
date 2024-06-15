#!/usr/bin/python3
import sys
import os
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'API')))

from api import route_manager

app = Flask(__name__)
route_manager(app)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
