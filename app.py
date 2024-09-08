import os
from models import db, Code, User
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    send_from_directory,
    jsonify,
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import urllib.parse

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


@app.route("/api/msg", methods=["GET"])
def msg():
    return "Hello World!"


@app.route("/api/sendEmailCode", methods=["GET"])
def sendCodeEmail():
    data = {
        "personalizations": [
            {
                "to": [{"email": f"{os.getenv('SENDGRID_TO_EMAIL')}"}],
            }
        ],
        "from": {"email": f"{os.getenv('SENDGRID_FROM_EMAIL')}"},
        "template_id": f"{os.getenv('SENDGRID_TEMPLATE_ID')}",
    }
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        print(e.message)
        return jsonify({"message": "Error sending email"}), 400


@app.route("/api/register", methods=["POST"])
def register():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    # Check if user already exists
    user = User.query.filter_by(Username=username).first()
    if user:
        return jsonify({"message": "User already exists!"}), 400

    # Create new user
    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()

    # Create JWT token
    access_token = create_access_token(
        identity={"username": new_user.Username, "email": new_user.Email}
    )
    return (
        jsonify(
            {
                "message": "Registration successful! Redirecting shortly...",
                "access_token": access_token,
            }
        ),
        200,
    )


@app.route("/api/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    # Check if user exists
    user = User.query.filter_by(Username=username).first()
    if user is None:
        return jsonify({"message": "User does not exist!"}), 400

    # Check if password is correct
    if not check_password_hash(user.PasswordHash, password):
        return jsonify({"message": "Invalid password!"}), 400

    # Create JWT token
    access_token = create_access_token(
        identity={"username": user.Username, "email": user.Email}
    )
    return jsonify({"message": "Login successful!", "access_token": access_token}), 200


@app.route("/api/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


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
