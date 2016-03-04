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

    def create_edition(self, **kwargs):
        """
        Convenience method for creating a new edition.
        """
        from .edition import Edition
        edition = Edition.create(
            book=self,
            title=kwargs.get('title') or self.title,
            subtitle=kwargs.get('subtitle') or self.subtitle,
            **kwargs
        )
        return edition
