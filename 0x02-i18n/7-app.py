#!/usr/bin/env python3
# Setting up a basic flask app.
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from pytz import UnknownTimeZoneError


# flask constructor
app = Flask(__name__)


# config class to store language and timezone
class config:
    # Setting languages
    LANGUAGES = ['en', 'fr']
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
    if user_id in users:
        return users[user_id]
    return None

# Function to get timezone (with validation)
@babel.timezoneselector
def get_timezone():
    # check if timezone is passed in URL
    timezone = request.args.get('timezone')

    # if timezone from URL is valid, use it
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

        # check if timezone is set in user settings
        user - get_user()
        if user and user.get("timezone"):
            try:
                pytz.timezone(user["timezone"])
                return user["timezone"]
            except UnknownTimeZoneError:
                pass

        # Default to UTC if no valid timezone found
        return app.config['TIMEZONE']


# Define the before_request function to set the user globally using flask.g
@app.before_request
def before_request():
    user = get_user()
    g.user = user


# Context Processor to make get_timezone globally available
@app.context_processor
def inject_timezone():
    return dict(get_timezone=get_timezone)


# Define a route for the root URL
@app.route('/')
def index():
    return render_template('7-index.html')


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
