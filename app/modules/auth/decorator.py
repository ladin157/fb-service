from functools import wraps

from app.modules.auth.auth_controller import AuthController
from utils.response import send_error

from flask import request


def token_required(f):
    """
    Check token for further actions.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        b = AuthController.check_token(request)
        if not b:
            return send_error(message="Please provide a valid token to continue.")
        return f(*args, **kwargs)

    return decorated
