from ..mixins.test import TestCaseMixin
from . import fixtures
import base64
from nose.plugins.attrib import attr


class LoginAuthTestCase(TestCaseMixin):

    def setUp(self):
        super().setUp()
        fixtures.typical_user()

    # @attr('single')
    def test_unauthorized(self):
        'Testing (views.login_auth.unauthorized)'
        response = self.client.get('/login_auth/get_auth_token')
        self.assert404(response)

    # @attr('single')
    def test_get_auth_token(self):
        'Testing (views.login_auth.get_auth_token)'
        login = base64.b64encode(bytes('alice:qqq', 'ascii')).decode('ascii')
        headers = {'Authorization': 'Basic ' + login}
        response = self.client.get(
            '/login/get-auth-token',
            headers=headers
        )
        self.assertEqual(len(response.json['token']), 122)
