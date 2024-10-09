from flask import Flask
from config import DevelopmentConfiguration


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfiguration)
    return app