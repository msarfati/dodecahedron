from dodecahedron.mixins.test import TestCaseMixin
from dodecahedron import models
import datetime
from nose.plugins.attrib import attr


class ModelsTestCase(TestCaseMixin):

    @attr('single')
    def test_demo_environment(self):
        genre = models.Genre.create(name="fiction")
        language_english = models.Language.create(name="English")
        language_german = models.Language.create(name="German")

        # Creat author
        author = models.Author.create(
            last_name="Eliot",
            first_name="George",
            dob=datetime.date(1819, 11, 22),
            dod=datetime.date(1880, 12, 22)
        )
        author = models.Author.create(
            last_name="Orwell",
            first_name="George",
            dob=datetime.date(1903, 7, 25),
            dod=datetime.date(1950, 1, 21)
        )

        # And the book, and its edition
        models.Book.create_book(
            title="Nineteen Eighty-Four",
            isbn='0547249640',
            published_date=datetime.date(1949, 6, 8),
            genre=genre,
            authors=[author],
            language=language_english,
        )

        translator = models.Author.create(
            last_name="Wagenseil",
            first_name="Kurt",
            dob=datetime.date(1904, 5, 26),
            dod=datetime.date(1988, 12, 14)
        )

        book = models.Book.find(title="Nineteen Eighty-Four")
        book.create_edition(
            book,
            title="Neunzehnhundertvierundachtzig",
            published_date=datetime.date(1981, 4, 19),
            isbn="3550063474",
            is_translation=True,
            language=language_german,
            secondary_authors=[translator],
        )

        self.assertIn(
            models.Author.query.filter_by(last_name="Orwell", first_name="George").first(),
            models.Book.query.filter_by(title="Nineteen Eighty-Four").first().authors,
            "Expected relationship holds (Orwell wrote 'Nineteen Eighty-Four')."
        )

        # Test Update
        author = models.Author.find(last_name="Orwell", first_name="George")
        author.update(**dict(last_name="Blair", first_name="Eric", middle_names="Arthur"))
        author = models.Author.find(last_name="Blair")
        self.assertEquals(author.first_name, "Eric", "Update successful")

        # Test Delete
        author = models.Author.find(last_name="Eliot", first_name="George")
        author.delete()
        self.assertIsNone(models.Author.find(last_name="Eliot", first_name="George"), "Delete successful")
