from dodecahedron import db
from dodecahedron.mixins.model import CRUDMixin, MarshmallowMixin


class Author(db.Model, CRUDMixin, MarshmallowMixin):
    __tablename__ = "author"
    id = db.Column(db.Integer(), primary_key=True)

    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    middle_names = db.Column(db.String(50))

    dob = db.Column(db.Date)
    'Date of birth'

    dod = db.Column(db.Date)
    'Date of death'
