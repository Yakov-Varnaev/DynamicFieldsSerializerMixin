class DynamicFieldsMixin(object):
    """
    A serializer mixin that takes an additional `fields` argument that controls
    which fields should be displayed.
    """

    @property
    def fields(self):
        """
        This mixin allows to use any serializer as an ordinary serializer
        in code and as dynamic serializer for responses.

        You can specify which fields you want to see in response via
        `fields` argument. If you want to specify more than one field,
        you should separate them with `,`.

        Example: ?fields=username,first_name,last_name
        """
        fields = super(DynamicFieldsMixin, self).fields

        # in case of calling serializer not from request cycle
        if not hasattr(self, '_context'):
            return fields

        try:
            request = self.context['request']
        except KeyError:
            return fields

        params = getattr(request, 'query_params')

        try:
            requested_fields = params.get('fields', None).split(',')
        except AttributeError:
            requested_fields = None

        try:
            excluded_fields = params.get('fields!', None).split(',')
        except AttributeError:
            excluded_fields = []

        # Leave only those fields, which are passed as `fields` params
        given_fields = set(fields.keys())
        if requested_fields is None:
            # in case no `fields` params were given
            allowed = given_fields
        else:
            allowed = set(requested_fields)

        # Remove those fields from response,
        # which are listed after `fields!` argument
        excluded = set(filter(None, excluded_fields))
        for field in given_fields:

            if field not in allowed or field in excluded:
                fields.pop(field, None)

        return fields
