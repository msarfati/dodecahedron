# -*- coding: utf-8 -*-abs
from dodecahedron import db
import datetime
import flask
from itsdangerous import (
    TimedJSONWebSignatureSerializer
    as Serializer, BadSignature, SignatureExpired)
from .mixins import ModelMixin
from passlib.apps import custom_app_context as pwd_context


class User(db.Model, ModelMixin):
    """
    Used for both users and applications.

    http://blog.miguelgrinberg.com/post/restful-authentication-with-flask
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime)

    def __init__(self, username, password):
        self.username = username
        self.hash_password(password)
        self.created = datetime.datetime.utcnow()
        flask.current_app.logger.debug("Created User object: {0}".format(username))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(flask.current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(flask.current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    @classmethod
    def register(cls, username, password, email=None, confirmed=False, groups=None):
        new_user = cls.User()


    @classmethod
    def add_system_users(cls):
        pass

# class Group