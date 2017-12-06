"""Create flask app
"""
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from .models import db
from .config import Config


def create_app(name=None, switch=None, http=None, **cfg):
    """Create Flask app
    """
    app = Flask(name or 'goview')
    app.config.from_object(Config)
    #
    # overwrite config with custom parameters
    app.config.update(cfg)
    #
    # register database & migrations
    Migrate(app, db)
    #
    # register api endpoints
    register_endpoints(app)
    #
    CORS(app)
    #
    return app


def register_endpoints(app):
    pass
