#!/usr/bin/env python3
""" Script for SessionAuth class definition that inherits drom Auth class"""

from api.v1.auth.auth import Auth
from typing import Dict
import uuid
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class definition"""
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ overloaded instance method that returns a User based on cookie"""
        session_id = self.session_cookie(request)
        if session_id is not None:
            user_id = self.user_id_for_session_id(session_id)
            if user_id is not None:
                return User.get(user_id)
        return