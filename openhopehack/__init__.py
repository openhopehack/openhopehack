"""Initialize Flask app."""

from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        # Import parts of our application
        from .base import base

        # Register Blueprints
        app.register_blueprint(base.base_bp, url_prefix="/")

        return app
