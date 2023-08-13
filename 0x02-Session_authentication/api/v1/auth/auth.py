#!/usr/bin/env python3
"""
    This class manages the API authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch
from os import getenv


class Auth:
    """
        Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Defines which routes don't need authentication
            Return: bool True is authenticated
        """
        if path is None or excluded_paths is None:
            return True
        elif path[-1] == '/':
            if path in excluded_paths:
                return False
        else:
            path += '/'
            if path in excluded_paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
            gets the authorization header
            Return: None
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Current user
            return: none
        """
        return None

    def session_cookie(self, request=None):
        """
            Returns a cookie value from a request
            Args:
                request
            Return:
                Session cookie
        """
        if request is None:
            return None
        else:
            session_env = getenv('SESSION_NAME', '_my_session_id')
            session_cookie = request.cookies.get(session_env)
            return session_cookie
