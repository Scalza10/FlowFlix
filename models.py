from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

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
    """
    Represents a user in the system.
    Attributes:
        Id (int): The unique identifier for the user.
        Username (str): The username of the user.
        Email (str): The email address of the user.
        PasswordHash (str): The hashed password of the user.
        CreatedAt (datetime): The date and time when the user was created.
        UpdatedAt (datetime): The date and time when the user was last updated.
    Methods:
        __init__(username, email, password):
            Initializes a new instance of the User class.
        __repr__():
            Returns a string representation of the User object.
    """
    __tablename__ = 'Users'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
    UpdatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __init__(self, username, email, password):
        self.Username = username
        self.Email = email
        self.PasswordHash = generate_password_hash(password)

    def __repr__(self) -> str:
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance.
        """
        return f'<User {self.username}>'