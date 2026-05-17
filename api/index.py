import os
import sys

# Add the project root to the sys.path to allow importing app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app

app = flask_app
handler = flask_app
application = flask_app
