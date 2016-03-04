from dodecahedron.mixins.test import TestCaseMixin
from dodecahedron import db, models
import datetime
from flask import Flask
from nose.plugins.attrib import attr


class BookTestCase(TestCaseMixin):

    # @attr('single')
    def test_sandbox(self):
        author = models.Author.create(
            last_name="Orwell",
            first_name="George",
            born=datetime.date(1903, 7, 25),
            died=datetime.date(1950, 1, 21)
        )
        book = models.Book.create(
            title="Nineteen Eighty-Four",
            isbn='0547249640',
            published_date=datetime.date(1949, 6, 8),
            published_city="London",
            authors=[author],
        )

        import ipdb; ipdb.set_trace()
        # book = models.Book()