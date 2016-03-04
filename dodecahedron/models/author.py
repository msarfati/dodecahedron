from .. import db
from ..mixins.model import CRUDMixin


class Author(db.Model, CRUDMixin):
    __tablename__ = "author"
    id = db.Column(db.Integer(), primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    middle_names = db.Column(db.String(50))

    born = db.Column(db.Date)
    died = db.Column(db.Date)
