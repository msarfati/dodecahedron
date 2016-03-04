# -*- coding: utf-8 -*-
from .. import db
from ..mixins.model import CRUDMixin


books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer(), db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer(), db.ForeignKey('author.id')))


class Book(db.Model, CRUDMixin):
    __tablename__ = "book"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.String(255))

    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    'Foreign Key for Lab'

    authors = db.relationship('Author',
        enable_typechecks=False,
        secondary=books_authors,
        # backref=db.backref('users', lazy='dynamic'),
    )
