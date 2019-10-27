from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# from flask_cors import CORS





login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# cors = CORS()



bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])


    #initializing flask Extensions

    # cors.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')


    from .requests import configure_request
    configure_request(app)


    return app