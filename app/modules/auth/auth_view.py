from flask import request
from flask_restx import Resource

from app.modules.auth.auth_controller import AuthController
from app.modules.auth.auth_dto import AuthDto
from app.modules.auth.decorator import token_required
from app.modules.user.user_dto import UserDto

api = AuthDto.api
_auth_login = AuthDto.model_login
# _user_info = UserDto.model_response


@api.route('/login')
class Login(Resource):
    '''
    API login
    '''

    # @api.expect(_auth)
    @api.expect(_auth_login)
    # @api.response(code=200, model=_user_info, description='Model for user response on login.')
    def post(self):
        """
        Login user to the system.
        -------------
        :param email: the email of the user.

        :param password: the password of the user.

        :return: All information of user if he logged in and None if he did not log in.
        """
        post_data = request.json
        controller = AuthController()
        return controller.login_user(data=post_data)

