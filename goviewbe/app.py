"""Create flask app
"""
from flask import Flask
from flask_migrate import Migrate

from .models import db
from .config import Config
from .api import api
from .web import web


def create_app(name=None, **cfg):
    """Create Flask app
    """
    app = Flask(name or 'goview')
    app.config.from_object(Config)
    #
    # overwrite config with custom parameters
    app.config.update(cfg)
    #
    # register database & migrations
    db.init_app(app)
    Migrate(app, db)
    #
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web)
    return app
