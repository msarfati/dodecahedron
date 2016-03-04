from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin

editions_authors = db.Table('editions_authors',
    db.Column('edition_id', db.Integer(), db.ForeignKey('edition.id')),
    db.Column('author_id', db.Integer(), db.ForeignKey('author.id')))


class Edition(db.Model, CRUDMixin):
    __tablename__ = "edition"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    isbn = db.Column(db.String(13))
    published_date = db.Column(db.Date)

    book = db.relationship(
        'Book',
        backref=db.backref(
            'edition',
            lazy='dynamic',
            cascade="delete, delete-orphan",
        )
    )

    book_id = db.Column(
        db.Integer,
        db.ForeignKey("book.id"),
        nullable=False,
        unique=True
    )

    language = db.relationship('Language', backref=db.backref('edition', lazy='dynamic'))
    language_id = db.Column(db.Integer, db.ForeignKey("Language.id"))
