from flask import Flask
from .routes import init_routes
from .models import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config.Config")

    db.init_app(app)
    init_routes(app)

    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    return app