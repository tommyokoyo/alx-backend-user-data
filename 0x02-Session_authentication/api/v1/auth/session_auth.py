#!/usr/bin/env python3
"""
    Session Authentication Module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
        Responsible for session Authentication
        Inherits From auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            creates a session ID for a user_id
            args:
                user_id: str - id of user
            return:
                Session id
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id: str = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Return User id based on the session id
            Args:
                session_id: str : session id
            Return:
                user_id: str : user id
        """
        if session_id is None or type(session_id) is not str:
            return None
        else:
            user_id: str = self.user_id_by_session_id.get(session_id)
            return user_id
