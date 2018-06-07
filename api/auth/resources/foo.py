from flask_restful import Resource


class Foo(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

    def post(self):
        pass
