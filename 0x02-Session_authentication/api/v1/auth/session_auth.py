#!/usr/bin/env python3
"""
    Session Authentication Module
"""
from api.v1.auth.auth import Auth
from typing import TypeVar


class SessionAuth(Auth):
    """
        Responsible for session Authentication
        Inherits From auth class
    """
