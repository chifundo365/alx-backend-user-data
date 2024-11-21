#!/usr/bin/env python3
"""
Api Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manage API Authentication
    """
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """ check if a path require authentication
        Return:
            - True | False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the requets authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user or None
        """
        return None
