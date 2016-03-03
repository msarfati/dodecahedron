# -*- coding: utf-8 -*-
from ..mixins import TestCaseMixin
from . import fixtures
import base64
from nose.plugins.attrib import attr
from werkzeug import Client
from werkzeug.datastructures import Headers


class ApiAccessTestCase(TestCaseMixin):

    def setUp(self):
        super().setUp()
        fixtures.typical_user()
        # self.base_url = "http://localhost:{}".format(self.app.config['PORT'])

    # @attr('single')
    def test_unauthorized(self):
        'Testing views.api_access.unauthorized'
        response = self.client.get('/login_auth/get_auth_token')
        self.assert404(response)

    @attr('single')
    def test_get_auth_token(self):
        'Testing views.api_access.get_auth_token'
        # headers = Headers()
        # headers.add('Authorization',
            # 'Basic ' + str(base64.b64encode(bytes('alice:qqq', 'utf-8'))))
        # response = Client.open(self.client, path='/api/get_auth_token',
            # headers=headers)
        # headers = \
        #     [('Authorization',
        #     'Basic ' + login)]

        login = str(base64.b64encode(bytes('alice:qqq', 'ascii')))
        # headers = {'Authorization': 'Basic ' + login}
        headers = Headers()
        headers.add('Authorization', 'Basic ' + login)
        response = self.client.get(
            '/login_auth/get-auth-token',
            headers=headers
        )
        print(response.data); assert False;
        # import ipdb; ipdb.set_trace()
