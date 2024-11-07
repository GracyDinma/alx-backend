#!/usr/bin/env python3
# Setting up a basic flask app.
from flask import Flask, render_template
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

# creating a get locale function with babel.localselector
@babel.localeselector
def get_locale():
    # Check if hte 'locale' parameter is in hte query string
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Use the parameter to find the best match for the user's language.
    return request.accept.languages.best_match(app.config['LANGUAGES'])


# Define a route for the root URL
@app.route('/')
def index():
    return render_template('4-index.html')


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
