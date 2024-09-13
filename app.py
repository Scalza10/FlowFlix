import os
from models import db
from flask import (
    Flask,
    render_template,
    send_from_directory,
)
from flask_jwt_extended import (
    JWTManager,
)
from flask_cors import CORS
import urllib.parse

# Import Blueprints
from _blueprints.auth import auth_bp
from _blueprints.email import email_bp
from _blueprints.codes import codes_bp

app = Flask(
    __name__, static_folder="./frontend/dist", template_folder="./frontend/dist"
)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = "potato123422"  # Necessary for session management
app.config["JWT_SECRET_KEY"] = "potato123422"  # Necessary for session management

jwt = JWTManager(app)

driver = "ODBC Driver 17 for SQL Server"

# Construct connection string
odbc_connect_str = (
    f"DRIVER={{{driver}}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"PORT=1433;"
    f"DATABASE={os.getenv('DB_DATABASE')};"
    f"UID={os.getenv('DB_USERNAME')};"
    f"PWD={os.getenv('DB_PASSWORD')};"
)

conn_params = urllib.parse.quote_plus(odbc_connect_str)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mssql+pyodbc:///?odbc_connect={conn_params}"

db.init_app(app)

# Register Blueprints for routes
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(email_bp, url_prefix="/api")
app.register_blueprint(codes_bp, url_prefix="/api")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    # If the path corresponds to a file in 'dist/static', serve it
    if (
        path.startswith("js/")
        or path.startswith("css/")
        or path.startswith("img/")
        or path.startswith("favicon.ico")
    ):
        return send_from_directory("./frontend/dist", path)
    # Otherwise, serve the index.html for SPA navigation
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
