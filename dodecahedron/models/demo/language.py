from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin


class Language(db.Model, CRUDMixin):
    __tablename__ = "language"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(15))
