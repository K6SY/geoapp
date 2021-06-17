from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here

    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    from .sig import sig as sig_blueprint 
    app.register_blueprint(sig_blueprint)

    from .admin import admin as admin_blueprint 
    app.register_blueprint(admin_blueprint)

    return app
