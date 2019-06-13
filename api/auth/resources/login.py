from flask_restful import Resource, reqparse
from flask import jsonify

from api.models.user import User


class LoginApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='用户名不能为空', location='json')
        self.reqparse.add_argument('password', type=str, required=True, help='密码不能为空', location='json')
        super(LoginApi, self).__init__()

    def get(self):
        return {'task': 'Say "Hello, World!"'}

    def post(self):
        args = self.reqparse.parse_args()
        username = args.get('username')
        password = args.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            token = user.generate_auth_token().decode('ascii')
            user.token = token

            return jsonify({'data': user.to_dict()})

        return {'errcode': 422, 'errmsg': '用户名或者密码不对'}, 422
