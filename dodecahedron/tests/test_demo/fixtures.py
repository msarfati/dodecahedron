from ... import models
import datetime


def populate_demo():
    typical_author()
    typical_authors()


def typical_author():
    return models.Author.find_or_create(
            last_name="Orwell",
            first_name="George",
            dob=datetime.date(1903, 7, 25),
            dod=datetime.date(1950, 1, 21),
        )


def typical_authors():
    authors = [
        dict(
            last_name="Doctorow",
            first_name="Cory",
            dob=datetime.date(1971, 7, 17)),
        dict(
            last_name="Heidegger",
            first_name="Martin",
            dob=datetime.date(1889, 9, 26),
            dod=datetime.date(1976, 5, 26)),
    ]

    for i in authors:
        models.Author.find_or_create(**i)
