from .demo import author


def init_api(api_extension):
    api_extension.add_resource(author.Author, "/api/author/<int:id>")
    api_extension.add_resource(author.Authors, "/api/authors")
