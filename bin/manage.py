#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand, upgrade

manager.add_command("shell", Shell(make_context=lambda: dict(app=app, db=db, models=models)))
manager.add_command("runserver", Server(port=app.config['PORT']))
manager.add_command("publicserver", Server(port=app.config['PORT'], host="0.0.0.0"))