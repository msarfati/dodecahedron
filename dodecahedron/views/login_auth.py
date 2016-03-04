from .. import auth, models
from flask import Blueprint, g, make_response, render_template
import json

login_auth = Blueprint('login_auth', __name__)
# This blueprint handles RESTful API authentication and token generation.


@auth.error_handler
def unauthorized():
    return make_response("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n""", 404)


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


@login_auth.route('/get-auth-token')
@auth.login_required
def get_auth_token():
    """
    Generates an authentication token for 600 seconds.
    :returns: json
    """
    token = g.user.generate_auth_token(600)
    return json.dumps({'token': token.decode('ascii'), 'duration': 600})


@login_auth.route('/resource')
@auth.login_required
def get_resource():
    return json.dumps({'data': 'Hello, %s!' % g.user.username}), 200


@login_auth.route('/sample')
def get_sample():
    return json.dumps(dict(msg='Hello'))
