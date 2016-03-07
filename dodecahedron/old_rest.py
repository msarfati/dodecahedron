from app import auth, db, models
import json
from flask.ext.restful import abort, Api, Resource, reqparse, fields, marshal


def get_Page_args(required=False):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=required, location='json')
    parser.add_argument('pos', type=str, required=required, location='json')
    args = parser.parse_args()
    return args


class Page(Resource):
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


class PageList(Resource):
    decorators = [auth.login_required]

    def post(self):
        '''
        Example:
            curl -u alice:qqq -X POST -H "content-type: application/json" -d '{"name": "Rest Test", "pos": "<1,1,1>"}' "http://localhost:55555/api/PageList"
        '''
        args = get_Page_args(required=True)
        obj = models.Page(**args)
        db.session.add(obj)
        db.session.commit()
        return json.dumps(obj.as_dict()), 201

    def get(self):
        page_list = [i.id for i in models.Page.query.all()]
        return json.dumps(page_list)
