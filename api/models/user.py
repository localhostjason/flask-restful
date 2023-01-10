from werkzeug.security import generate_password_hash, check_password_hash
# from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from authlib.jose import jwt, JoseError

from .. import db

import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    _password = db.Column(db.String(128))

    token = db.Column(db.String(128))

    @property
    def test(self):
        return 'id:{}'.format(self.id)

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def generate_auth_token(self):
        """生成用于邮箱验证的JWT（json web token）"""
        # 签名算法
        header = {'alg': 'HS256'}
        # 用于签名的密钥
        key = current_app.config['SECRET_KEY']
        # 待签名的数据负载
        now = datetime.datetime.now()
        exp = now + datetime.timedelta(hours=8)
        data = {'id': self.id, 'exp': exp}
        # data.update(**kwargs)

        return jwt.encode(header=header, payload=data, key=key)

        # s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        # return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        key = current_app.config['SECRET_KEY']

        try:
            data = jwt.decode(token, key)
        except:
            return None
        return User.query.get(data['id'])
