from config import app_config
from spotify_app import auth
from flask import Flask


def create_app(test_config=None):
    # initial creation and configuration of app
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.register_blueprint(auth.bp)

    return app
