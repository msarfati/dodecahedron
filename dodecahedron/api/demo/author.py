from .. import models
from marshmallow_sqlalchemy import ModelSchema
from flask.ext.restful import abort, Api, Resource, reqparse, fields, marshal


class AuthorSchema(ModelSchema):
    class Meta:
        model = models.Author

class Author(Resource):
    decorators = [auth.login_required]


    def get(self, id):
        page = models.Page.query.filter(models.Page.id == id).first()
        if page:
            return json.dumps(page.as_dict())
        else:
            abort(404, message="object does not exist")

    def put(self, id):
        args = get_Page_args(required=True)
        page = models.Page.query.filter(models.Page.id == id).first()
        if page:
            page.name = args['name']
            page.pos = args['pos']
            db.session.add(page)
            db.session.commit()
            return json.dumps(page.as_dict())

    def delete(self, id):
        obj = models.Clinic.find(id=id)
        if obj:
            return obj.delete()
        else:
            abort(404, message="object does not exist")
