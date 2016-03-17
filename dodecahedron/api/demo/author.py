from ... import auth
from ... import models
from ...schemas import AuthorSchema
from flask.ext.restful import abort, Api, Resource, reqparse, fields, marshal


class Author(Resource):
    # decorators = [auth.login_required]

    def get(self, id):
        author = models.Author.query.filter(models.Author.id == id).first()
        try:
            return author.dumps()
        except:
            abort(404, message="object does not exist")

    def put(self, id):
        args = get_Author_args(required=True)
        author = models.Author.query.filter(models.Author.id == id).first()
        if author:
            author.name = args['name']
            author.pos = args['pos']
            db.session.add(author)
            db.session.commit()
            return json.dumps(author.as_dict())

    def delete(self, id):
        obj = models.Clinic.find(id=id)
        if obj:
            return obj.delete()
        else:
            abort(404, message="object does not exist")


class Authors(Resource):
    # decorators = [auth.login_required]

    def get(self):
        pass

    def post(self):
        pass
