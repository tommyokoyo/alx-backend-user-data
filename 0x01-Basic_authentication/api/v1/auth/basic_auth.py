#!/usr/bin/env python3
"""
    Basic Auth module
"""
import binascii
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """
        Basic auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
            Extracts the base64 part of theAuthorization
            header for a basic authentication
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[0:6] != 'Basic ':
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
            Decodes the base64 authorization header
            return: decoded value of Base64
        """
        if (base64_authorization_header is None or type
                (base64_authorization_header) is not str):
            return None
        else:
            try:
                return b64decode(base64_authorization_header,
                                 validate=True).decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str):
            return 'None', 'None'
        elif ':' in decoded_base64_authorization_header:
            user_email = decoded_base64_authorization_header.split(':')[0]
            user_pass = decoded_base64_authorization_header.split(':')[1]
            return user_email, user_pass
        else:
            return 'None', 'None'
