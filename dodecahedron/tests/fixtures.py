# -*- coding: utf-8 -*-
from .. import models


def typical_user():
    username = 'alice'
    if not models.User.query.filter_by(username=username).first():
        return models.User.register(
            username=username,
            password='qqq',
            confirmed=True,
        )
