from flask import request
from flask_restx import Resource, reqparse

from app.modules.auth.decorator import token_required
from .phone_controller import PhoneController
from .phone_dto import PhoneDto

api = PhoneDto.api

parser = reqparse.RequestParser()
parser.add_argument('address', type=str, required=True, help='The address to searching for the phone number.')


@api.route('/getphonenumber')
@api.expect(parser)
class PhoneSearch(Resource):
    @token_required
    def get(self):
        """
        Search phone number given by the address.
        ---------------------
        :address: The address to search

        :return: The (formatted) phone number.
        """
        args = request.args
        controller = PhoneController()
        return controller.search_phone_number(args=args)
