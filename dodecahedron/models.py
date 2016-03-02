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
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime())
    active = db.Column(db.Boolean())

    # def __init__(self, username, password):
    #     self.username = username
    #     self.hash_password(password)
    #     self.created = datetime.datetime.utcnow()
    #     flask.current_app.logger.debug("Created User object: {0}".format(username))

    def __repr__(self):
        return self.username

    # Password methods
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
    def register(cls, username, password, email=None, confirmed=False, roles=None):
        """
        Create a new user account.

        :param email: the email address used to identify the account
        :type email: string
        :param password: the plaintext password for the account
        :type password: string
        :param confirmed: whether to confirm the account immediately
        :type confirmed: boolean
        :param roles: a list containing the names of the Roles for this User
        :type roles: list(string)
        """
        new_user = cls(
            username=username,
            email=email,
            password_hash=pwd_context.encrypt(password),
        )
        db.session.commit()
        if confirmed:
            new_user.confirm()
        if roles:
            for role_name in roles:
                new_user.add_role(role_name)
        flask.current_app.logger.debug("Created user {0}".format(username))
        return new_user

    def confirm(self):
        self.confirmed_at = datetime.datetime.now()
        self.active = True

    def add_role(self, role_name):
        pass
        # self.role = role_name
        # db.session.add(self)
        # db.session.commit()

    @classmethod
    def add_system_users(cls):
        pass


class Role(db.Model, ModelMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
