from flask import Blueprint
from controllers import get_data, get_info

data_bp = Blueprint("data", __name__, url_prefix="/data")

data_bp.route("/get-data", methods=["GET"])(get_data)
data_bp.route("/get-info", methods=["GET"])(get_info)
