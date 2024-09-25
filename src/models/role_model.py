from src.db import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String)

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return f'<Role {self.role_name}>'

    def to_dict(self):
        return {
            "role_id": self.id,
            "role_name": self.role_name
        }
