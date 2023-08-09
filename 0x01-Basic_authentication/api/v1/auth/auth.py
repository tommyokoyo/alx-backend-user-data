#!/usr/bin/env python3
"""
    This class manages the API authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
        Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Require Auth
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
            Require Auth
            Return: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Current user
            return: none
        """
        return None
