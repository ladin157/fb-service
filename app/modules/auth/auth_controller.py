from app import db
from app.modules.user.user import User
from settings.config import Config
from utils.response import send_error
from utils.util import log, encode_auth_token, decode_auth_token


class AuthController:
    """
    This class is used to authenticate and authorize the user.
    """
    def login_user(self, data):
        """
        Login user handling.
        """
        try:
            # print(data)
            user = User.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                auth_token = encode_auth_token(user_id=user.id, user_role=user.admin)
                # user.active = True
                # db.session.commit()
                if auth_token:
                    log("info",user.email,"Logged In")
                    return {'access_token': auth_token.decode('utf8')}
                    # return {'access_token': auth_token}
            else:
                return send_error(
                    message='Email hoac Mat khau khong dung, vui long thu lai')  # Email or Password does not match')
        except Exception as e:
            print(e.__str__())
            return send_error(
                message='Khong the dang nhap, vui long thu lai.')

    @staticmethod
    def check_token(req):
        '''
        Check token for genuine user.
        '''
        auth_token = None
        api_key = None
        # auth = False
        if 'X-API-KEY' in req.headers:
            api_key = req.headers['X-API-KEY']
        if 'Authorization' in req.headers:
            auth_token = req.headers.get('Authorization')
        if not auth_token and not api_key:
            # auth = False
            return None
        if api_key is not None:
            auth_token = api_key

        return str(auth_token).__eq__(Config.AUTH_TOKEN)

    @staticmethod
    def get_logged_user(req):
        '''
        User information retrieving.
        '''
        auth_token = None
        api_key = None
        # auth = False
        if 'X-API-KEY' in req.headers:
            api_key = req.headers['X-API-KEY']
        if 'Authorization' in req.headers:
            auth_token = req.headers.get('Authorization')
        if not auth_token and not api_key:
            # auth = False
            return None, 'You must provide a valid token to continue.'
        if api_key is not None:
            auth_token = api_key
        user_id, message = decode_auth_token(auth_token=auth_token)
        if user_id is None:
            return None, message
        try:
            user = User.query.filter_by(id=user_id).first()
            return user, None
        except Exception as e:
            print(e.__str__())
            return None, message
