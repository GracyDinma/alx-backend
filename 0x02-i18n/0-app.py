#!/usr/bin/env python3
# Setting up a baaaaasic flask app.
from flask import Flask, render_template

# flask constructor
app = Flask(__name__)

# route() function tells the application to render
# index.html template.


@app.route('/')
def index():
    return render_template('index.html')


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
