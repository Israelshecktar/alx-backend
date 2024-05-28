#!/usr/bin/env python3
"""
A basic Flask application for displaying a welcoming message.
This module creates a simple web server with Flask to demonstrate
a 'Hello, world' message.
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    This function is mapped to the root URL and returns the content of
    the index.html template which displays a welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
