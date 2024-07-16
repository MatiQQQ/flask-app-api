from .auth_routes import auth_bp
from .data_routes import data_bp


def init_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(data_bp)
