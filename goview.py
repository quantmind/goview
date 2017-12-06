#!/usr/bin/env python3
"""
Script that gunicorn imports to find the application that it will start.
Creates a flask application object and db object
"""
from flask import current_app

import goviewbe


app = goviewbe.create_app()


@app.cli.command()
def safe_upgrade():
    """Safe upgrade tables waiting for db to be available
    """
    goviewbe.upgrade_db(current_app)
