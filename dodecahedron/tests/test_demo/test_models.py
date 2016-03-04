from dodecahedron.mixins.test import TestCaseMixin
from dodecahedron import db, models
import datetime
from flask import Flask
from nose.plugins.attrib import attr


class ModelsTestCase(TestCaseMixin):

    # @attr('single')
    def test_demo_environment(self):
        models.Genre.create(name="fiction")
        models.Language.create(name="English")
        models.Language.create(name="German")

        author = models.Author.create(
            last_name="Orwell",
            first_name="George",
            dob=datetime.date(1903, 7, 25),
            dod=datetime.date(1950, 1, 21)
        )

        book = models.Book.create(
            title="Nineteen Eighty-Four",
            authors=[author],
        )

        edition = models.Book.create(
            book=book,
            title=book.title,
            isbn='0547249640',
            published_date=datetime.date(1949, 6, 8),
        )
        book = models.Book.find()

        translator = models.Author.create(
            last_name="Orwell",
            first_name="George",
            dob=datetime.date(1903, 7, 25),
            dod=datetime.date(1950, 1, 21)
        )

        import ipdb; ipdb.set_trace()
        # book = models.Book()