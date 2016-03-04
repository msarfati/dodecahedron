from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin


class Genre(db.Model, CRUDMixin):
    __tablename__ = "genre"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
