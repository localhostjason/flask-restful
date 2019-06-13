from flask import Blueprint
from ..app import api
from .resources.login import LoginApi
from .resources.logout import LogOutApi

api_auth = Blueprint('auth', __name__)

api.add_resource(LoginApi, '/login')
api.add_resource(LogOutApi, '/logout')

api.init_app(api_auth)

"""Initialize this class with the given :class:`flask.Flask`
        application or :class:`flask.Blueprint` object.

        :param app: the Flask application or blueprint object
        :type app: flask.Flask
        :type app: flask.Blueprint

        Examples::

            api = Api()
            api.add_resource(...)
            api.init_app(app)

        """
