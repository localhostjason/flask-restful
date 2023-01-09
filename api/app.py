# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from .base_model import BaseModel

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
api = Api()


def create_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, static_url_path='')
    app.config.from_object(Config)

    Config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .resources.auth import api_auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api')

    from .resources.users import api_user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api')

    from cmds.db import db_cmd
    app.register_blueprint(db_cmd)

    from cmds.linux_server import server_cmd
    app.register_blueprint(server_cmd)
    return app
