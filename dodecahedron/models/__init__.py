from .role import Role
from .user import User

# If demo context, then import demo models
import flask
if flask.current_app.config["DEMO_MODE"] == True:
    from .demo import *
