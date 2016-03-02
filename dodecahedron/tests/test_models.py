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
        role1 = models.Role(name="Role1")
        role2 = models.Role(name="Role2")
        role3 = models.Role(name="Role3")
        db.session.add_all([role1, role2, role3])
        db.session.commit()

        user = models.User.register(
            username='alice',
            password='qqq',
            confirmed=True,
            roles=[role1, role2],
        )
        user = models.User.query.filter_by(username='alice').first()

        self.assertEqual(user.username, "alice", "Obj attributes readible.")
        self.assertIn(user.roles, role1)
