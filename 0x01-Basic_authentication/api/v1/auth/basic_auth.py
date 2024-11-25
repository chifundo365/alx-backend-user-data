#!/usr/bin/env python3
""" Basic authentication """
from .auth import Auth
import re


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
