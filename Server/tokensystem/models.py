from datetime import datetime
from tokensystem import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.id}', '{self.username}', '{self.email}')"


class Token(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.String(100), nullable=False, unique=True)
  created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return f"Token('{self.id}', '{self.value}')"
