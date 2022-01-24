# note that the first flask is lowercase 
# and the second is upper.
from flask import Flask

def create_app():
    """Create and configure an instance
    of the flask application."""
    app = Flask(__name__)
    
    @app.route("/")
    def root():
        return "Hello, world!"
    return app