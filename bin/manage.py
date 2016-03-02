#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')

from dodecahedron import create_app, db, models
from flask.ext.script import Manager, Shell, Server

app = create_app()

manager = Manager(app)
manager.add_command("shell", Shell(make_context=lambda: dict(app=app, db=db, models=models)))
manager.add_command("runserver", Server(port=app.config['PORT']))
manager.add_command("publicserver", Server(port=app.config['PORT'], host="0.0.0.0"))


@manager.command
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def populate_db():
    models.User.add_system_users()

if __name__ == "__main__":
    manager.run()
