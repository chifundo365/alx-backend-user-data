#!/usr/bin/env python3
""" session_exp_auth module """
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth
        Session authentication with Expiration
    """
    def __init__(self):
        """ init """
        try:
            s_duration = os.environ.get("SESSION_DURATION")
            s_duration = int(s_duration)
            self.session_duration = s_duration
        except Exception as e:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ creates a session """
        session_id = super().create_session(user_id)

        if not session_id:
            return None
        session_dictionary = {
                "user_id": user_id,
                "created_at": datetime.now()
                }
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ retrieves the user id og a session id """
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id(session_id)
            if self.session_duration <= 0:
                return session_dict.get('user_id')
            if 'created_at' not in session_dict:
                return None
            cur_time = datetime.now()
            time_span = timedelta(second=self.session_duration)
            exp_time = session_dict.get('created_at') + time_span
            if exp_time < cur_time:
                return None
            return session_dict.get('user_id')
