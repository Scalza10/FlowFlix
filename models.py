from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Codes(db.Model):
    __tablename__ = 'Codes'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Code = db.Column(db.String(50), nullable=False)
    StartDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ExpirationDate = db.Column(db.DateTime, nullable=False)

    def __init__(self, code, start_date, expiration_date):
        self.Code = code
        self.StartDate = start_date
        self.ExpirationDate = expiration_date

    def __repr__(self):
        return f'<Code {self.Code}>'
