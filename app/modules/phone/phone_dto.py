from flask_restx import Namespace, fields

from app.modules.common.dto import Dto


class PhoneDto(Dto):
    name = 'phone'
    api = Namespace(name)
    model_request = api.model('phone_request', {
        'address': fields.String(required=False)
    })
    model_response = api.model('phone_response', {
        'phone': fields.String(required=False)
    })
