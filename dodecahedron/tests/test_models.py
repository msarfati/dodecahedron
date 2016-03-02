# -*- coding: utf-8 -*-
from ..mixins import TestCaseMixin
from dodecahedron import db, models
from flask import Flask
from nose.plugins.attrib import attr


class UserTestCase(TestCaseMixin):

    # @attr('single')
    def test_register(self):
        'Testing models.User.register'
        # Create a dummy role
        role1 = models.Role(name="role1")
        role2 = models.Role(name="role2")
        role3 = models.Role(name="role3")
        db.session.add_all([role1, role2, role3])
        db.session.commit()

        user = models.User.register(
            username='alice',
            password='qqq',
            confirmed=True,
            roles=["role1", "role2"],
        )
        user = models.User.query.filter_by(username='alice').first()

        self.assertEqual(user.username, "alice", "Obj attributes readible.")
        self.assertIn(role1, user.roles)
        self.assertIn(role2, user.roles)

    # @attr('single')
    def test_add_system_users(self):
        models.User.add_system_users()
        admin, guest = map(
            lambda username: models.User.query.filter_by(username=username).first(),
            ['admin', 'guest']
        )
        self.assertIn(models.Role.query.filter_by(name="admin").first(), admin.roles)
        self.assertIn(models.Role.query.filter_by(name="guest").first(), guest.roles)
