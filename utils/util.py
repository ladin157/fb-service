# -*- coding: utf-8 -*-

"""
File: util.py
Purpose: This file contains some useful and essential function utilities.

This is the applications utilities.
"""
import hashlib
from datetime import datetime, timedelta

import jwt

from settings.config import Config


def encode_filename_sha(filename):
    '''
    Encode the filename (without extension).

    :param filename: The filename.

    :return: The encoded filename.
    '''
    encoded = hashlib.sha224(filename.encode('utf8')).hexdigest()
    return encoded


def encode_filename_md5(filename):
    encoded = hashlib.md5(filename.encode('utf8')).hexdigest()
    return encoded

def encode_file_name(filename):
    '''
    Encode the filename (without extension).

    :param filename: The filename.

    :return: The encoded filename.
    '''
    encoded = hashlib.sha224(filename.encode('utf8')).hexdigest()
    return encoded



def encode_auth_token(user_id):
    '''
    Generate the Auth token.

    :param user_id: The user's ID to generate token

    :return:
    '''
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30, seconds=5),
            'iat': datetime.utcnow(),
            'sub': user_id,
        }
        return jwt.encode(
            payload,
            Config.SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        print(e.__str__())
        return None


def decode_auth_token(auth_token):
    """
    Validates the auth token

    :param auth_token:

    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, Config.SECRET_KEY)
        return payload['sub'], ''  # return the user_id
    except jwt.ExpiredSignatureError:
        return None, 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return None, 'Invalid token. Please log in again.'


def log(level, user, message):
    try:
        line = ""
        line += str(datetime.utcnow()) + '\t\t'
        line += level + '\t\t'
        line += user + '\t\t'
        line += message + '\n'

        fw = open(Config.LOG_PATH, 'a', encoding='utf-8')
        fw.write(line)
        fw.close()

    except Exception as e:
        print(e.__str__())