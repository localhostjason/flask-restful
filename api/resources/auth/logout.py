from flask_restful import Resource, reqparse
from flask import jsonify

from api.models.user import User
from api.auth_token import token_auth


class LogOutApi(Resource):
    decorators = [token_auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('token', type=str, required=True, help='token不能为空', location='json')
        super(LogOutApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        token = args.get('token')

        user = User.query.filter_by(token=token).first()
        if not user:
            return {'errcode': 422, 'errmsg': 'Token失效或者不对'}, 422

        user.token = None
        return jsonify({})
