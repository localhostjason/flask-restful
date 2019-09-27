from flask_restful import fields, marshal_with, reqparse, Resource
from api.models import User as UM


def valid_email(str):
    return True


def email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if valid_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username',
    location='json', required=True,
    help='The user\'s username',
)
post_parser.add_argument(
    'email', dest='email',
    type=email, location='json',
    required=True, help='The user\'s email',
)
post_parser.add_argument(
    'user_priority', dest='user_priority',
    type=int, location='json',
    default=1, choices=range(5), help='The user\'s priority',
)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'user_priority': fields.Integer,
    'custom_greeting': fields.FormattedString('Hey there {username}!'),
    'date_created': fields.DateTime,
    'date_updated': fields.DateTime,
    'links': fields.Nested({
        'friends': fields.Url('user_friends'),
        'posts': fields.Url('user_posts'),
    }),
}

user_f = {
    'username': fields.String,
    'uri': fields.Url()
}


class User(Resource):

    @marshal_with(user_f)
    def post(self):
        args = post_parser.parse_args()
        # user = create_user(args.username, args.email, args.user_priority)
        print(args)
        user = UM.query.first()
        return user

    @marshal_with(user_f)
    def get(self):
        return {}
