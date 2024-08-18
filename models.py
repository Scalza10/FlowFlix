from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Code(db.Model):
    __tablename__ = 'Codes'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Code = db.Column(db.String(50), nullable=False)
    StartDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    ExpirationDate = db.Column(db.DateTime, nullable=False)

    def __init__(self, code, start_date, expiration_date):
        self.Code = code
        self.StartDate = start_date
        self.ExpirationDate = expiration_date

    def __repr__(self):
        return f'<Code {self.Code}>'

class User(db.Model):
    __tablename__ = 'Users'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
    UpdatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __init__(self, username, email, password_hash):
        self.Username = username
        self.Email = email
        self.PasswordHash = password_hash

    def __repr__(self):
        return f'<User {self.Username}>'