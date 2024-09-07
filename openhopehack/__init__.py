"""Initialize Flask app."""

from flask import Flask
from flask_dance.contrib.github import make_github_blueprint


def create_app(config: object | str) -> Flask:
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = app.config["SECRET_KEY"]

    # Load the configuration
    app.config.from_object(config)

    with app.app_context():
        # Import parts of our application
        from .base import base

        # GitHub OAuth setup
        github_blueprint = make_github_blueprint(
            client_id=app.config["GITHUB_CLIENT_ID"],
            client_secret=app.config["GITHUB_CLIENT_SECRET"],
        )

        # Register Blueprints
        app.register_blueprint(base.base_bp, url_prefix="/")
        app.register_blueprint(github_blueprint, url_prefix="/login")

        return app
