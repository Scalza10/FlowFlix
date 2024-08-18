import os
from models import Code, db
from flask import Flask, render_template, redirect, url_for, request, flash, session
import urllib.parse

app = Flask(__name__)
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

@app.route('/')
def home():
    if 'username' in session:
        first_code = Code.query.first()
        return f"Welcome, {session['username']}! <br> This is your code {first_code.Code} <br><a href='/logout'>Logout</a>"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
