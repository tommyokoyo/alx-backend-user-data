"""
    This class manages the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
        Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Require Auth
            Return: bool True is authenticated
        """
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
