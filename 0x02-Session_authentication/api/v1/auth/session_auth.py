#!/usr/bin/env python3
""" Session Authentication """
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates Assesiob ID for a user_id """
        if not user_id or not isinstance(user_id, str):
            return None
        ss_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[ss_id] = user_id

        return ss_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """" Retrieves the user_id given the sesssion_id """
        if not session_id or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        print(f"user_id {user_id}")
        try:
            return User.get(user_id)
        except Exception as e:
            return None

    def destroy_session(self, request=None):
        """ Destroys the usersession/ logout """
        if request is None:
            return False
        s_id = self.session_cookie(request)

        if not s_id:
            return False
        if not self.user_id_for_session_id(s_id):
            return False
        del self.user_id_by_session_id[s_id]

        return True
