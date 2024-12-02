#!/usr/bin/env python3
""" Moudule of Users views """
from flask import request, jsonify, make_response
import os
from api.v1.views import app_views
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """ login and Session creation View """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400

    user = User.search({'email': email})

    if not user:
        return jsonify({'error': 'no user found for this email'})
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth

    ss_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(os.environ.get('SESSION_NAME'), ss_id)
    return response
