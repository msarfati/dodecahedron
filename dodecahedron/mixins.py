#!/usr/bin/env python
import re


class ModelMixin(object):

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if not re.match("^_", k)}
