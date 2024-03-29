import copy

from flask_restful import Api, Resource

from .utils import null_view, ismatch


class CustomApi(Api):
    def __init__(self, app=None):
        super(CustomApi, self).__init__(app=app)

    def add_resource(self, resource, *urls, **kwargs):
        if kwargs.get('demo_dict'):
            resource = get_demo_resource(resource, kwargs['demo_dict'])
        kwargs.pop('demo_dict', None)
        super(CustomApi, self).add_resource(resource, *urls, **kwargs)


def get_demo_resource(resource, demo_dict):
    if not resource:
        resource = type('DemoResource', (Resource, ), dict())

    for method, values in demo_dict.iteritems():
        method = method.lower()
        old_method = getattr(resource, method, null_view)
        setattr(resource, method, get_demo_view(values, old_method))

    return resource


def get_demo_view(demo_responses, default_view=null_view):
    def required_view(self, *args, **kwargs):
        # fetching args in order from kwargs
        if not demo_responses.get('keys'):
            raise Exception("No Keys specified in Demo Dict Method")
        mapped_args = [kwargs[x] for x in demo_responses['keys']]

        pattern_responses = copy.copy(demo_responses)
        pattern_responses.pop('keys')

        for pattern, response in pattern_responses.iteritems():
            if ismatch(pattern, mapped_args):
                return response
        return default_view(self, *args, **kwargs)
    return required_view


