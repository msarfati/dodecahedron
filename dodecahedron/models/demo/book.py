from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin


books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer(), db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer(), db.ForeignKey('author.id')))


class Book(db.Model, CRUDMixin):
    __tablename__ = "book"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    isbn = db.Column(db.String(13))
    published_date = db.Column(db.Date)

    authors = db.relationship('Author',
        enable_typechecks=False,
        secondary=books_authors,
        # backref=db.backref('users', lazy='dynamic'),
    )

    genre = db.relationship('Genre', backref=db.backref('book', lazy='dynamic'))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
