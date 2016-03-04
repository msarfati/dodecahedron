# -*- coding: utf-8 -*-
from .. import create_app, db
from flask import current_app
from flask.ext.testing import TestCase


class TestCaseMixin(TestCase):
    """
    Use with flask.ext.testing.TestCase
    """

    def create_app(self):

        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        # super().create_app()
        return app

    def setUp(self):
        """
        Prepare for a test case.
        """
        db.create_all()
        current_app.logger.debug("setup complete")
        super().setUp()

    def tearDown(self):
        """
        Clean up after a test case.
        """
        db.session.remove()
        db.drop_all()
        super().tearDown()
