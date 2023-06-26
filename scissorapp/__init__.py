from flask import Flask
from .extensions import db, migrate, login_manager, bcrypt
from .routes import short, cache
from dotenv import load_dotenv
import os

login_manager.login_view = 'short.login'


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config['DEBUG'] = app.config.get('DEBUG', False)

    load_dotenv()

    app.config.from_pyfile(config_file)

    secret_key = os.getenv('SECRET_KEY')

    app.config['SECRET_KEY'] = secret_key

    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)

    app.static_folder = 'static'

    app.register_blueprint(short)

    return app

app = create_app()
app.debug = True
