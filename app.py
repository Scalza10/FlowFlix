import os
from models import Code, db
from flask import Flask, render_template, redirect, url_for, request, flash, session, send_from_directory
from flask_cors import CORS
import urllib.parse

app = Flask(__name__,
            static_folder = "./frontend/dist",
            template_folder = "./frontend/dist")

CORS(app, resources={r"/api/*": {"origins": "*"}})
app.secret_key = 'potato123422'  # Necessary for session management

# Dummy user data
users = {'user1': 'password123',
         'user2': 'password456',
         'user3': 'password789'
    }


driver="ODBC Driver 17 for SQL Server"

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

app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={conn_params}"
db.init_app(app)

# @app.route('/')
# def home():
#     if 'username' in session:
#         first_code = Code.query.first()
#         return f"Welcome, {session['username']}! <br> This is your code {first_code.Code} <br><a href='/logout'>Logout</a>"
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in users and users[username] == password:
#             session['username'] = username
#             flash('Login successful!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid credentials. Please try again.', 'danger')
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('login'))

@app.route('/api/msg', methods=['GET'])
def msg():
    return "Hello World!"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # If the path corresponds to a file in 'dist/static', serve it
    if path.startswith('js/') or path.startswith('css/') or path.startswith('img/') or path.startswith('favicon.ico'):
        return send_from_directory('./frontend/dist', path)
    # Otherwise, serve the index.html for SPA navigation
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
