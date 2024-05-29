#!/usr/bin/env python3
"""
This Flask app is configured to support English and French using Flask-Babel
for i18n.
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    config file for module config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Render the index.html template with a welcome message.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
