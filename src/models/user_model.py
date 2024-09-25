from src.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    social_networks = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __init__(self, username: str, email: str, password: str, social_networks: dict):
        self.username = username
        self.email = email
        self.password = password
        self.social_networks = social_networks

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "social_networks": self.social_networks
        }