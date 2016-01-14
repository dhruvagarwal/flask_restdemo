from flask_restful import Api, Resource

from .utils import null_view, ismatch

class CustomApi(Api):
    def __init__(self, app=None):
        super(CustomApi, self).__init__(app=app)

    def proxy_add_resource(self, resource, *urls, **kwargs):
        if kwargs.get('demo_dict'):
            # according to demo_dict, register methods in the resource
            # call a method which returns a resource(extended), with the
            # demo_dict options.
            resource = get_demo_resource(resource, kwargs['demo_dict'])
        super(CustomApi, self).add_resource(resource, *urls, **kwargs)


def get_demo_resource(resource, demo_dict):
    if not resource:
        resource = type('DemoResource', (Resource, ), dict())

    for method, values in demo_dict.iteritems():
        # old_meth = resource.meth['method']
        # new_meth = get_demo_view(values, old_meth)
        # resource.meth['method'] = new_meth
        pass
    return resource


def get_demo_view(demo_responses, default_view=null_view):
    # generate a method which matches the args combo
    # and returns the given response.
    # also get url-param objects as this func params.
    def required_view(self, *args):
        for pattern, response in demo_responses.iteritems():
            if ismatch(pattern, args):
                return response
        return default_view
    return required_view
