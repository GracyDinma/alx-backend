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


# configure the flask app
app = Flask(__name__)
app.config.from_object(config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """_summary_

    Returns:
        _type_:_description_
    """
    return request.accept.languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """default route

    Returns:
        html: homepage
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port='5000', debug=True)
