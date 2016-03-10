from . import ma
from . import models
from .factories import _schema_factory

model_list = (
    'Author',
    'Book',
    'Edition',
    'Genre',
    'Language'
)

schemas = map(lambda i: _schema_factory(i), model_list)


# class AuthorSchema(ma.ModelSchema):

#     class Meta:
#         model = models.Author
#         # additional = (
#         #     "last_name",
#         #     "first_name",
#         #     "middle_names",
#         #     "dob",
#         #     "dod",
#         # )


# class BookSchema(ma.ModelSchema):

#     class Meta:
#         model = models.Book


# class EditionSchema(ma.ModelSchema):

#     class Meta:
#         model = models.Book
