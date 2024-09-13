from flask import Blueprint
from _controllers.email_controller import send_email

email_bp = Blueprint('email', __name__)

email_bp.route("/sendEmailCode", methods=["GET"])(send_email)