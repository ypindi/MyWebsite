from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'anusha_yashwanth'
    # encrypts the cookies and session data related to our website
    # in production, do not share this secret key with anybody
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # database is stored in this location
    db.init_app(app)

    from .views import views
    from .auth import auth
    from flask_login import LoginManager

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note
    # from .models import User, Note
    # or can write import .models also works this is so that we can create our database

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    # the 3 lines above are telling flask how we load a user.
    # By default, it will look for the primary key.
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        # we are passing app because we need to tell sqlalchemy which app we are creating
        # the database for
        print('Created Database!')

