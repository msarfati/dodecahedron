# -*- coding: utf-8 -*-
from ..mixins import TestCaseMixin
from dodecahedron import db, models
from flask import Flask
from nose.plugins.attrib import attr


class UserTestCase(TestCaseMixin):

    @attr('single')
    def test_register(self):
        'Testing models.User.register'
        # Create a dummy role
        role = models.Role(name="Generic Role", description="This is a generic role for testing.")
        db.session.add(role)
        db.session.commit()

        user = models.User.register(
            username='alice',
            password='qqq',
            confirmed=True,
            roles=[role],
        )
        user = models.User.query.filter_by(username='alice').first()
        self.assertEqual(user.username, "alice", "Obj attributes readible.")
        import ipdb; ipdb.set_trace()
        # self.assertEqual(user.username, "alice", "Obj attributes readible.")
