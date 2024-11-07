#!/usr/bin/env python3
# Setting up a basic flask app.
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from datetime import datetime
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
    return request.args.get('timezone', 'UTC')


# Function to get the current time in the correct timezone
def get_current_time():
    # Get the timezone from the get_timezone function
    timezone = get_timezone()
    try:
        tz = pytz.timezone(timezone)
        local_time = datetime.now(tz)
        return local_time.strftime('%b %d, %Y, %I:%M:%S %p')
    except pytz.UnknownTimeZoneError:
        return datetime.now(pytz.utc).strftime('%b %d, %Y, %I:%M:%S %p')


# Make the function available globally in jinja template
app.jinja_env.globals.update(get_current_time=get_current_time)


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
    return render_template('index.html')


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
