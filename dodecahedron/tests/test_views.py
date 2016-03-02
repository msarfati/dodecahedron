# -*- coding: utf-8 -*-
from ..mixins import TestCaseMixin
from . import fixtures
import base64
from nose.plugins.attrib import attr
from werkzeug.datastructures import Headers


class ApiAccessTestCase(TestCaseMixin):

    def setUp(self):
        super().setUp()
        fixtures.typical_user()
        # self.base_url = "http://localhost:{}".format(self.app.config['PORT'])

    # @attr('single')
    def test_unauthorized(self):
        'Testing views.api_access.unauthorized'
        response = self.client.get('/api/get_auth_token')
        self.assert404(response)

    @attr('single')
    def test_verify_password(self):
        'Testing views.api_access.verify_password'
        headers = [('Authorization',
                    'Basic ' + str(base64.b64encode(bytes('alice:qqq', 'utf-8'))))]
        response = self.client.get(
            '/api/get_auth_token',
            headers=headers
        )
        print(response.data); assert False;
        import ipdb; ipdb.set_trace()

    # @attr('single')
    def test_get_auth_token(self):
        'Testing views.api_access.get_auth_token'
        pass
