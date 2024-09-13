from flask import Blueprint
from _controllers.codes_controller import generate_code

codes_bp = Blueprint('code', __name__)

# Define routes for code-related operations if needed