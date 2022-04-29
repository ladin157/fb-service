from flask_restx import Api

from app.modules import ns_upload, ns_user, ns_auth

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


def init_api():
    api = Api(title='FunnelBeam APIs',
              version='0.1',
              description='The FunnelBeam APIs',
              authorizations=authorizations,
              security='apikey'
              )
    api.add_namespace(ns_auth, '/api/v1/auth')
    api.add_namespace(ns_upload, '/api/v1/uploader')
    api.add_namespace(ns_user, '/api/v1/user')

    return api
