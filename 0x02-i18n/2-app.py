#!/usr/bin/env python3
"""
This flask app is configured to support english and french language using \
         flask babel. it determines the best match for locale
"""

from flask import Flask, render_template, request
from flask_babel import babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name)
app.config_from_object(Config)

babel = bable(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages from the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template with a welcome message.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
