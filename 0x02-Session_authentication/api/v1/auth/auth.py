#!/usr/bin/env python3
"""
Api Authentication
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Manage API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if a path is not in the excluded paths
        Return:
            - True or False
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        if path[-1] != "/":
            path = path + "/"

        if path == '/api/v1/status/':
            return False
        if path in excluded_paths:
            return False
        for ex_path in excluded_paths:
            if ex_path[-1] == "*":
                _ex_path = ex_path[0: -1] + ".*"
            if re.search(_ex_path, path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the requets Authorization header
        """
        if not request:
            return None
        header = request.headers.get("Authorization", None)

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user or None
        """
        return None
