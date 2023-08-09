#!/usr/bin/env python3
"""
    Basic Auth module
"""
from api.v1.auth.auth import Auth


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
