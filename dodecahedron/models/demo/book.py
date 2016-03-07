from .edition import Edition
from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin
import flask

books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer(), db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer(), db.ForeignKey('author.id')))


class Book(db.Model, CRUDMixin):
    __tablename__ = "book"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text)
    subtitle = db.Column(db.Text)

    authors = db.relationship('Author',
        enable_typechecks=False,
        secondary=books_authors,
        # backref=db.backref('users', lazy='dynamic'),
    )

    genre = db.relationship('Genre', backref=db.backref('book', lazy='dynamic'))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))

    @classmethod
    def create_book(cls, **kwargs):
        get_args = lambda model, kwargs: {k: v for k, v in kwargs.items() if k in model.__table__.columns.keys()}
        book_args = get_args(cls, kwargs)
        edition_args = get_args(Edition, kwargs)
        import ipdb; ipdb.set_trace()

        book = cls.create(**book_args)
        edition = cls.create_edition(book, **edition_args)
        return [book, edition]

    @classmethod
    def create_edition(cls, book, **kwargs):
        """
        Convenience method for creating a new edition.
        """
        # import ipdb; ipdb.set_trace()
        get_arg = lambda key: kwargs.pop(key) if key in kwargs else getattr(book, key)
        edition = Edition.create(
            book=book,
            title=get_arg('title'),
            subtitle=get_arg('subtitle'),
            **kwargs
        )
        return edition
