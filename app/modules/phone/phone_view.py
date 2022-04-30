from flask_restx import Resource, reqparse
from .phone_dto import PhoneDto
from .phone_controller import PhoneController
from app.modules.auth.decorator import admin_token_required, token_required

api = PhoneDto.api
topic_request = PhoneDto.model_request
topic_response = PhoneDto.model_response

parser = reqparse.RequestParser()
parser.add_argument('address', type=str, required=False, help='The name of the topic')


@api.route('/getphonenumber')
@api.expect(parser)
class PhoneSearch(Resource):
    @token_required
    @api.response(code=200, model=topic_response, description='Model for success response.')
    def get(self):
        """
        Search phone number given by the address.
        ---------------------
        :address: The address to search

        :return: The (formated) phone number.
        """
        args = parser.parse_args()
        controller = PhoneController()
        return controller.search_phone_number(args=args)
