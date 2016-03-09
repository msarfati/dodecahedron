from . import ma
from . import models


class AuthorSchema(ma.ModelSchema):

    class Meta:
        model = models.Author
        # additional = (
        #     "last_name",
        #     "first_name",
        #     "middle_names",
        #     "dob",
        #     "dod",
        # )


class BookSchema(ma.ModelSchema):

    class Meta:
        model = models.Book
