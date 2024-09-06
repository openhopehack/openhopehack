from .base import base_bp


def init_app(app):
    app.register_blueprint(base_bp)
