from flask import Flask
import logging
from app.configuration import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.logger.setLevel(logging.INFO)

    from app.routes.train_details import train_details_bp
    app.register_blueprint(train_details_bp)

    return app