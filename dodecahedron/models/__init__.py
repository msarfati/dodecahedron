from .role import Role
from .user import User

# If demo context, then import demo models
# import ipdb; ipdb.set_trace()
# from .. import app
# if app.config["DEMO_MODE"] == True:
from .demo import *
