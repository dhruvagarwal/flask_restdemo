from flask_restful import Api, Resource

from .utils import null_view, ismatch

class CustomApi(Api):
    def __init__(self, app=None):
        super(CustomApi, self).__init__(app=app)

    def proxy_add_resource(self, resource, *urls, **kwargs):
        if kwargs.get('demo_dict'):
            resource = get_demo_resource(resource, kwargs['demo_dict'])
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
    def required_view(self, *args):
        for pattern, response in demo_responses.iteritems():
            if ismatch(pattern, args):
                return response
        return default_view(args)
    return required_view
