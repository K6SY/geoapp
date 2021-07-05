from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

login_manager = LoginManager()
login_manager.login_view = 'main.login'

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #injections de dépendance
    db.init_app(app)
    # attach routes and custom error pages here

    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    from .sig import sig as sig_blueprint 
    app.register_blueprint(sig_blueprint)

    from .admin import admin as admin_blueprint 
    app.register_blueprint(admin_blueprint)

    login_manager.init_app(app) 

    return app
