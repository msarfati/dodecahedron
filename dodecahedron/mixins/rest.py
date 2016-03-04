

class RestCollectionMixin(object):
    """
    Used for Collections
    """
    def post(self):
        """
        Returns 201 (created), and in the header, the fully qualified domain name of what was created, eg:
            201, https://dodecahedron.com/api/customers/my_customer
        """
        return 201


class RestInstanceMixin(object):
    pass
