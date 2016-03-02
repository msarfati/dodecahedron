# -*- coding: utf-8 -*-
from .. import auth, models
from flask import Blueprint, g, make_response
import json

api_access = Blueprint('api_access', __name__)
# This blueprint handles RESTful API authentication and token generation.


@auth.error_handler
def unauthorized():
    return make_response("<html><body><h1>404 Not Found</h1></body></html>", 404)


@auth.verify_password
def verify_password(username_or_token, password):
    "Verifies credientials."
    # first try to authenticate by token
    user = models.User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = models.User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@api_access.route('/get_auth_token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return json.dumps({'token': token.decode('ascii'), 'duration': 600})
