from ..mixins.test import TestCaseMixin
from nose.plugins.attrib import attr


class DodecahedronTestCase(TestCaseMixin):

    # @attr('single')
    def test_testing(self):
        self.assertEqual(2, 1+1)
