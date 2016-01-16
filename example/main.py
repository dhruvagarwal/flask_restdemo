from flask import Flask
from flask_restful import Resource

from flask_restdemo.flask_restdemo import CustomApi

app = Flask(__name__)
api = CustomApi(app)

class A(Resource):

    def get(self, a, b):
        return {'a': a, 'b': b}

    def post(self, a, b):
        return {'a': a, 'b': b}

d = {
        'get': {
            (1, 'g*'): {
                'message': 'yo agga'
            },
            (2, 'b'): {
                'm': 'Hey!'
            }
        },
        'post': {
            (1, 'a'): {
                'message': 'Something'
            }
        }
    }

class B(Resource):
    def get(self):
        return {'message': 'BP'}

B_route_dict = {
            'get': {
                (): {'message': 'JD'}
            }
        }

api.add_resource(A, '/check/<int:a>/<string:b>', demo_dict=d)
api.add_resource(B, '/check', demo_dict=B_route_dict)

app.run(debug=True, host='0.0.0.0', threaded=True)
