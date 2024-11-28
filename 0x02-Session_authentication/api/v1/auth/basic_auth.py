#!/usr/bin/env python3
""" Basic authentication """
import re
import base64
from typing import TypeVar
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic Authentication class """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header
        """
        header = authorization_header
        if not header or not isinstance(header, str):
            return None
        if re.search(r'^Basic', header):
            return header[6:]
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Decodes a Base64 Authorization header """
        header = base64_authorization_header
        if not header or not isinstance(header, str):
            return None
        try:
            return base64.b64decode(header).decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ Passes user email and password from base64 decoded values """
        header = decoded_base64_authorization_header
        if not header or not isinstance(header, str) or ":" not in header:
            return None, None
        return tuple(header.split(":", 1))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        Searches for a user Given the Credentials

        Returns:
            - User Object that matches the credentials.
        """
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        try:
            objects = User.search({"email": user_email})
        except Exception as e:
            return None
        for user in objects:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user for a request """
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        decoded_h = self.decode_base64_authorization_header(base64_header)
        user_credentials = self.extract_user_credentials(decoded_h)

        email, password = user_credentials
        return self.user_object_from_credentials(email, password)
