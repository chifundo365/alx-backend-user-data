#!/usr/bin/env python3
"""
Api Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manage API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if a path is not in the excluded path
        Return:
            - True or False
        """
        if path[-1] != "/":
            path = path + "/"
        if path is not in excluded_paths or path is None:
            return True
        if excluded_paths is None or not len(excluded_paths):
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the requets authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user or None
        """
        return None
