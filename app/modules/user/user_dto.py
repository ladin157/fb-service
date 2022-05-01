from flask_restx import Namespace, fields

from app.modules.common.dto import Dto


class UserDto(Dto):
    name = 'user'
    api = Namespace(name)
    model_request = api.model('user_request', {
        'firstname': fields.String(required=False, default=''),
        'lastname': fields.String(required=False, default=''),
        'email': fields.String(required=True),
        'password': fields.String(required=True),
        'admin': fields.Boolean(required=False, default=False),
    })

    model_response = api.model('user_response', {
        'id': fields.Integer(readonly=True),
        'firstname': fields.String(required=False),
        'lastname': fields.String(required=False),
        'age': fields.String(required=False),
        'email': fields.String(required=False),
        'admin': fields.Boolean(required=False, default=False),
    })
