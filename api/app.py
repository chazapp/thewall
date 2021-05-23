import os
from flask import Flask 
from flask_cors import CORS
from dotenv import load_dotenv
from api.api import API

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(API)
    try:
        os.mkdir("./medias/")
    except OSError as e:
        pass
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=8080, debug=True)