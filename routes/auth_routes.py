from flask import Blueprint
from controllers import register_user, login_user, protected

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.route("/register", methods=["POST"])(register_user)
auth_bp.route("/login", methods=["POST"])(login_user)
auth_bp.route("/protected", methods=["GET"])(protected)
