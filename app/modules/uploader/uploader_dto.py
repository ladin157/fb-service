from flask_restx import Namespace, fields

from app.modules.common.dto import Dto


class UploaderDto(Dto):
    name = 'uploader'
    api = Namespace(name=name)
    model = api.model(name, {
        'url': fields.String(required=True, description = 'The url to file store in server.')
    })
