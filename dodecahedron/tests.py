# -*- coding: utf-8 -*-
from app import app, db, models
from flask import Flask
from flask.ext.testing import TestCase
from nose.plugins.attrib import attr


class AppTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()
        db.session.commit()

    # @attr('single')
    def test_rest_page(self):
        self.assertEqual(2, 1+1)
        # CREATE
        self.client
        # READ (list)

        # READ (id)

        # UPDATE

        # DELETE
