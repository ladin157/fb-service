from flask_restx import Resource, reqparse
from flask import request
from .phone_dto import PhoneDto
from .phone_controller import PhoneController
from app.modules.auth.decorator import admin_token_required, token_required

api = PhoneDto.api
# phone_request = PhoneDto.model_request
phone_response = PhoneDto.model_response

parser = reqparse.RequestParser()
parser.add_argument('address', type=str, required=True, help='The address to searching for the phone number.')
# parser.add_argument('user_id', type=int, required=False, help='Search topic by user_id (who created topic)')
# parser.add_argument('parent_id', type=int, required=False, help='Search all sub-topics which belongs to the parent ID.')


@api.route('/getphonenumber')
@api.expect(parser)
class PhoneSearch(Resource):
    # @token_required
    # @api.expect(parser)
    # @api.response(code=200, model=phone_response, description='Model for success response.')
    def get(self):
        """
        Search phone number given by the address.
        ---------------------
        :address: The address to search

        :return: The (formatted) phone number.
        """
        # data = api.payload
        print(request.args)
        args = request.args
        # args = parser.parse_args()
        controller = PhoneController()
        return controller.search_phone_number(args=args)
