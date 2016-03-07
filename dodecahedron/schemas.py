from . import models
from marshmallow_sqlalchemy import ModelSchema


class AuthorSchema(ModelSchema):

    def __init__(self):

        class Meta:
            print(dir(self))
            print(self.name)
            model = models.Author
