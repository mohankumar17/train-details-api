from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.train_details import train_details_bp
    app.register_blueprint(train_details_bp)

    return app