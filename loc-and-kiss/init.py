from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'database'))
    db_path = os.path.join(db_directory, 'lak_database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.template_folder = "../templates/"
    app.static_folder = "../static/"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for game parts of app
    from game import game as game_blueprint
    app.register_blueprint(game_blueprint)

    # blueprint for profile routes in our app
    from profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    # blueprint for dev routes in our app
    from dev import dev as dev_blueprint
    app.register_blueprint(dev_blueprint)

    return app