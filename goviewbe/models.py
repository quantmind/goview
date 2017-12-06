import logging
import time

from sqlalchemy.exc import OperationalError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import upgrade


db = SQLAlchemy()
LOGGER = logging.getLogger("goview")


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    completed = db.Column(db.DateTime)


def upgrade_db(app):
    with app.app_context():
        delay = 1
        while True:
            try:
                if app.config['SWITCH'] == 'test':
                    db.create_all()
                else:
                    upgrade()
                break
            except OperationalError:
                LOGGER.warning(
                    'Waiting for database connection for %s seconds', delay
                )
                time.sleep(delay)
                delay = min(delay * 2, 30)
