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
        print("inside the function")
        if not session_id:
            return None
        user_id = super().user_id_for_session_id(session_id)

        if not user_id:
            return None
        if type(user_id) == dict:
            print(f"user_dict: {user_id}")
            if self.session_duration <= 0:
                return user_id.get('user_id')
            if not user_id.get('created_at'):
                return None
            t_delta = timedelta(seconds=self.session_duration)
            now  = datetime.now()
            if user_id.get('created_at') + t_delta > now:
                print(f"created_at + duration: {user_id.get('created_at') + t_delta}")
                print(f"now: {now}")
                return user_id.get('user_id')
            return None
        return None
                  
