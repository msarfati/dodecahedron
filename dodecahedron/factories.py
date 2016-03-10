from . import ma
from . import models


def _schema_factory(model_name):
    '''
    Factory for building schemas.

    :param model_name: name of the model
    :type model_name: str
    '''
    return type(
        model_name + 'Schema',
        (ma.ModelSchema,),
        {'Meta': type('Meta', (object, ), {'model': getattr(models, model_name)})}
    )
