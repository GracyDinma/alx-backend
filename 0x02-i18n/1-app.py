#!/usr/bin/env python3
"""A basic Flask web app serves a simple HTML page.
"""


from flask import Flask, render_template
from flask_babel import Babel


# config class to store language and timezone
class config:
    """_summary_

    Returns:
        _type_:_description_
    """
    LANGUAGES = ['en', 'fr']
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


# flask constructor
app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@app.route('/')
def index():
    """Render the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
