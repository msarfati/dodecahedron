from . import ma
from . import models
from .factories import _schema_factory
import sys

model_list = (
    'Author',
    'Book',
    'Edition',
    'Genre',
    'Language'
)


def _build_schemas():
    """
    Builds schemas based on `model_list`. Assumes models are exposed in dodacahedron.models.

    May override these schemas, following:
        https://marshmallow-sqlalchemy.readthedocs.org/en/latest/
    """
    for i in model_list:
        setattr(
            sys.modules[__name__],  # gets the reference to the current module
            i + 'Schema',
            _schema_factory(i)
        )

_build_schemas()
