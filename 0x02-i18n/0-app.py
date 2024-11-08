#!/usr/bin/env python3
"""A basic Flask web app serves a simple HTML page.
"""


from flask import Flask, render_template

# Create an instance of the flask class
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Render the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
