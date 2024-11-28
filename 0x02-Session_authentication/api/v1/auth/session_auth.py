#!/usr/bin/env python3
""" Session Authentication """
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentication class """
    user_id_by_session = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates Assesiob ID for a user_id """
        if not user_id or not isinstance(user_id, str):
            return None
        ss_id = uuid.uuid4()
        SessionAuth.user_id_by_session[ss_id] = user_id

        return ss_id

