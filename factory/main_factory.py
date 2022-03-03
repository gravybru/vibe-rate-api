from flask import Flask
from flask_restful import Api
from controllers.vibe_controller import VibeRateController

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(VibeRateController, "/vibe")

    return app