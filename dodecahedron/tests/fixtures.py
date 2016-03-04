from .. import models
import datetime


def typical_user():
    username = 'alice'
    if not models.User.query.filter_by(username=username).first():
        return models.User.register(
            username=username,
            password='qqq',
            confirmed=True,
        )


def typical_author():
    return models.Author.find_or_create(
            last_name="Orwell",
            first_name="George",
            born=datetime.date(1903, 7, 25),
            died=datetime.date(1950, 1, 21)
        )


def typical_dataset():
    models.Author.create
    models.Book.create
