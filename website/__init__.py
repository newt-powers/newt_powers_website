from flask import Flask

def create_app():
    app = Flask(__name__)
    # encrypt/secure session data and cookies, character for secret key
    app.config['SECRET_KEY'] = 'secrets_are_stupid'

    return app