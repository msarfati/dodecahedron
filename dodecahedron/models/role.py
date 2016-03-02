# -*- coding: utf-8 -*-
from dodecahedron import db
from ..mixins import ModelMixin


class Role(db.Model, ModelMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return "<Role={}>".format(self.username)
