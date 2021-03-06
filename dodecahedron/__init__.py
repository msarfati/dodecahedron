from flask import Flask

app_instance = None

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

from flask_marshmallow import Marshmallow
ma = Marshmallow()

from flask.ext.restful import Api
rest_api = Api()


class Dodecahedron:

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, name=None):
        if not name:
            name = __name__

        self.app = Flask(name)

        self.app.config.from_envvar('SETTINGS')

        self.init_logs()

        self.init_database()

        self.init_blueprints()

        self.init_schemas()

        from .api import init_api
        self.init_api(init_api)

    def init_blueprints(self):
        from .views.login_auth import login_auth
        self.app.register_blueprint(login_auth, url_prefix="/login")

    def init_database(self):
        db.app = self.app
        db.init_app(self.app)

    def init_logs(self):
        import logging
        handler = logging.FileHandler(self.app.config['LOG'])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        self.app.logger.addHandler(handler)
        if self.app.config.get("LOG_LEVEL") == "DEBUG":
            self.app.logger.setLevel(logging.DEBUG)
        elif self.app.config.get("LOG_LEVEL") == "WARN":
            self.app.logger.setLevel(logging.WARN)
        else:
            self.app.logger.setLevel(logging.INFO)
        self.app.logger.info('Startup with log: %s' % self.app.config['LOG'])

    def init_api(self, api_map=None):
        # import ipdb; ipdb.set_trace()
        if api_map:
            api_map(rest_api)
        rest_api.init_app(self.app)
        return rest_api

    def init_schemas(self):
        ma.init_app(self.app)


def create_app():
    """
    Application factory.

    http://flask.pocoo.org/docs/0.10/patterns/appfactories/
    """
    global app_instance
    if not app_instance:
        app_instance = Dodecahedron()
        app_instance.init_app()
    return app_instance.app
