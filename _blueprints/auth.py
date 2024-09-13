from flask import Blueprint
from _controllers.auth_controller import register_user, login_user, protected_route

auth_bp = Blueprint('auth', __name__)

auth_bp.route("/register", methods=["POST"])(register_user)
auth_bp.route("/login", methods=["POST"])(login_user)
auth_bp.route("/protected", methods=["GET"])(protected_route)