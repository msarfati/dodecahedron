from ... import models
import datetime


def populate_demo():
    typical_author()


def typical_author():
    return models.Author.find_or_create(
            last_name="Orwell",
            first_name="George",
            dob=datetime.date(1903, 7, 25),
            dod=datetime.date(1950, 1, 21),
        )
