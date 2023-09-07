from config import app_config
from spotify_app import (
    db_setup, auth
)
from flask import Flask
from sqlalchemy import URL


def create_app(test_config=None):

    # Create app and load configuration
    app = Flask(__name__)
    app.config.from_object(app_config)
    if app.config['APP_MODE'] != 'PROD':
        app.config['FLASK_DEBUG'] = True
        app.config['SQLALCHEMY_ECHO'] = True  # Log statements to default log handler

    # Setup and configure db
    app.config['SQLALCHEMY_DATABASE_URI'] = URL.create(
        drivername=app.config['DB_DIALECT'],
        username=app.config['DB_USER'],
        password=app.config['DB_PASS'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        database=app.config['DATABASE'],
        query=app.config['DB_QUERY']
    )
    db_setup.db.init_app(app)

    with app.app_context():
        if app.config['APP_MODE'] != 'PROD':
            db_setup.db.drop_all()  # Drop all is fine as using a separate clean database
        db_setup.db.create_all()  # Setup tables based on models if they don't currently exist

    # Blueprint registering
    app.register_blueprint(auth.bp)

    return app
