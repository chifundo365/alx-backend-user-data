#!/usr/bin/env python3
""" Basic authentication """
from .auth import Auth
import re
import base64


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
        if not header or not isinstance(header, str) or not ":" in header:
            return None, None
        return tuple(header.split(":", 1))
