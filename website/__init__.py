from flask import Flask

def create_app():
    app = Flask(__name__)
    # encrypt/secure session data and cookies, character for secret key
    app.config['SECRET_KEY'] = 'secrets_are_stupid'

    # import views, auth blueprints
    from .views import views
    from .auth import auth

    # Register with flask application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
