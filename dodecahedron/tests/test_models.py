# -*- coding: utf-8 -*-
from .mixins import TestCaseMixin
from dodecahedron import models
from flask import Flask
from nose.plugins.attrib import attr


class UserTestCase(TestCaseMixin):

    @attr('single')
    def test_register(self):
        'Testing models.User.register'
        user = models.User.register(
            username='alice',
            password='qqq',
            confirmed=True,
        )

        user = models.User.query.filter_by(username='alice')
        self.assertIsNotNone(user, "User retrievable")
