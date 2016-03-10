from .. import db
import flask


class CRUDMixin:
    """
    Convenience functions for CRUD operations.

    Taken from `flask-diamond <https://github.com/diamond-org/flask-diamond/blob/develop/flask_diamond/mixins/crud.py>`.
    """

    __table_args__ = {'extend_existing': True}

    @classmethod
    def find(cls, **kwargs):
        """
        Find an object in the database with certain properties.

        :param kwargs: the values of the object to find
        :type kwargs: dict
        :returns: the object that was found, or else None
        """

        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_or_create(cls, _commit=True, **kwargs):
        """
        Find an object or, if it does not exist, create it.

        :param kwargs: the values of the object to find or create
        :type kwargs: dict
        :returns: the object that was created
        """

        obj = cls.find(**kwargs)
        if not obj:
            obj = cls.create(_commit=_commit, **kwargs)
        return obj

    @classmethod
    def get_by_id(cls, id):
        """
        Retrieve an object of this class from the database.

        :param id: the id of the object to be retrieved
        :type id: integer
        :returns: the object that was retrieved
        """

        if any(
            (isinstance(id, str) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, _commit=True, **kwargs):
        """
        Create a new object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was created
        """

        instance = cls(**kwargs)
        obj = instance.save(_commit)
        flask.current_app.logger.debug("create %s" % str(obj))
        return obj

    def update(self, _commit=True, **kwargs):
        """
        Update this object with new values.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was updated
        """

        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return _commit and self.save() or self

    def save(self, _commit=True):
        """
        Save this object to the database.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: the object that was saved
        """

        db.session.add(self)
        if _commit:
            db.session.commit()
        return self

    def delete(self, _commit=True):
        """
        Delete this object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: whether the delete was successful
        """

        db.session.delete(self)
        return _commit and db.session.commit()

    def __repr__(self):
        return "<{}(id={})>".format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()


class MarshmallowMixin:

    def __schema__(self):
        "Returns a Schema object based on the model name."
        from .. import schemas
        schema_name = type(self).__name__ + "Schema"
        return getattr(schemas, schema_name)() if hasattr(schemas, schema_name) else None

    # dump
    def dump(self):
        "serialize the Model object as a python object"
        return self.__schema__().dump(self).data

    def dumps(self):
        "serialize the Model object as a JSON string"
        return self.__schema__().dumps(self).data

    def dumpf(self, file_handle):
        "write a Model object to file_handle as a JSON string"
        file_handle.write(self.dumps())

    # load

    @classmethod
    def load(cls, python_obj):
        "create a Model object from a python object"
        obj = cls.__schema__().load(python_obj)
        return cls.create(**obj.data)

    @classmethod
    def loads(cls, buf):
        "create a Model object from a JSON-encoded string"
        obj = cls.__schema__().loads(buf)
        return cls.create(**obj.data)

    @classmethod
    def loadf(cls, file_handle):
        "create a Model object from a file_handle pointing to a JSON file"
        return cls.loads(file_handle.read())

    # dump_all

    @classmethod
    def dump_all(cls):
        "write all objects of Model class to an array of python objects"
        return cls.__schema__().dump(cls.query.all(), many=True).data

    @classmethod
    def dumps_all(cls):
        "write all objects of Model class to a JSON-encoded array"
        return cls.__schema__().dumps(cls.query.all(), many=True).data

    @classmethod
    def dumpf_all(cls, file_handle):
        "write all objects of Model class to file_handle as JSON"
        file_handle.write(cls.dumps_all())

    # load_all

    @classmethod
    def load_all(cls, python_objects):
        "create objects of Model class from an array of python objects"
        objs = cls.__schema__().load(python_objects, many=True)
        for obj in objs.data:
            cls.create(_commit=False, **obj)
        db.session.commit()
        db.session.flush()

    @classmethod
    def loads_all(cls, buf):
        "create objects of Model class from a string containing an array of JSON-encoded objects"
        objs = cls.__schema__().loads(buf, many=True)
        for obj in objs.data:
            cls.create(_commit=False, **obj)
        db.session.commit()
        db.session.flush()

    @classmethod
    def loadf_all(cls, file_handle):
        "create objects of Model class from a file containing an array of JSON-encoded objects"
        cls.loads_all(file_handle.read())
