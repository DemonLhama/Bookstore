from bookstore.db import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    activated = db.Column(db.Boolean, default=False)

    def __repr__(self, email, username, password_hash, activated):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.activated = activated

    def json(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "activated": self.activated
        }

    @classmethod
    def find_user_id(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()