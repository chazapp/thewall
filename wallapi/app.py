import os
from flask import Flask
from flask_cors.extension import CORS
from config import DevelopmentConfig
from database import db, migrate
from api.api import API


def create_app():
    app = Flask(__name__)
    CORS(app)
    if os.environ['FLASK_ENV'] == 'development':
        app.config.from_object(DevelopmentConfig())
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(API)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
