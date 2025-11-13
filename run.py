"""
Entry point for Flask application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Flask File Explorer -  Modified!</h1><p>Server is running</p>'

@app.route('/about')
def about():
    return '<h1>About</h1><p>This is a file directory explorer built with Flask.</p>'


if __name__ == '__main__':
    app.run(debug=True)
