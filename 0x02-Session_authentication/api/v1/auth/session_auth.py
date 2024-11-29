#!/usr/bin/env python3
""" Session Authentication """
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates Assesiob ID for a user_id """
        if not user_id or not isinstance(user_id, str):
            return None
        ss_id = uuid.uuid4()
        SessionAuth.user_id_by_session_id[ss_id] = user_id

        return ss_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """" Retrieves the user_id given the sesssion_id """
        if not session_id or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
