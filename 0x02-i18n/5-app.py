#!/usr/bin/env python3
# Setting up a basic flask app.
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


# flask constructor
app = Flask(__name__)


# config class to store language and timezone
class config:
    # Setting languages
    LANGUAGES = ['en', 'fr']
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


# Set up app's configuration with config class
app.config.from_object(config)

# Instantiate the Babel object
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define the get_user function to fetch a user from the mock "database"
def get_user():
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


# Define the before_request function to set the user globally using flask.g
@app.before_request
def before_request():
    user = get_user()
    g.user = user

# creating a get locale function with babel.localselector
@babel.localeselector
def get_locale():
    # Check if hte 'locale' parameter is in hte query string
    if g.user and g.user['locale']:
        return g.user['locale']
    # Use the parameter to find the best match for the user's language.
    return request.accept.languages.best_match(app.config['LANGUAGES'])


# Define a route for the root URL
@app.route('/')
def index():
    return render_template('5-index.html')


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
