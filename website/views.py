from flask import Blueprint

# Blueprint for flask application
views = Blueprint('views', __name__)


# Function will run whenever we go to the slash route
@views.route('/')
def home():
    return "<h1>Test</h1>"