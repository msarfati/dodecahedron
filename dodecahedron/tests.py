# -*- coding: utf-8 -*-
from .mixins import TestCaseMixin
from flask import Flask
from nose.plugins.attrib import attr


class DodecahedronTestCase(TestCaseMixin):

    # @attr('single')
    def test_testing(self):
        self.assertEqual(2, 1+1)

    @attr('single')
    def test_users(self):
        
        # CREATE
        self.client
        # READ (list)

        # READ (id)

        # UPDATE

        # DELETE
