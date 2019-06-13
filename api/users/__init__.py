from flask import Blueprint
from api.app import api
from api.auth_token import token_auth
from api.errors import *

from .resources.users import User

api_user = Blueprint('users', __name__)

api.add_resource(User, '/user')

api.init_app(api_user)


@api_user.before_request
@token_auth.login_required
def before_request():
    pass


@api_user.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
