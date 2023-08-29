#!/usr/bin/env python3
"""
    handles routes for all session authentication
"""
from os import getenv
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """
        POST /auth_session/login
        Return:
            session token
    """
    user_email = request.form.get('email')
    user_pass = request.form.get('password')
    if user_email is None or user_email == '':
        return jsonify({"error": "email missing"}), 400
    elif user_pass is None or user_pass == '':
        return jsonify({"error": "password missing"}), 400
    else:
        users_found = User.search({"email": user_email})

        if not users_found:
            return jsonify({"error":
                                "no user found for this email"}), 404
        else:
            for user in users_found:
                if user.is_valid_password(user_pass):
                    from api.v1.app import auth
                    session_id = auth.create_session(user.id)
                    response = jsonify(user.to_json())
                    response.set_cookie(getenv('SESSION_NAME'),
                                        session_id)
                    return response
                else:
                    return jsonify({"error":
                                        "wrong password"}), 401

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
        DELETE /auth_session/logout
        Return:
            {}
    """
    from api.v1.app import auth
    to_delete_token = auth.destroy_session(request)
    if to_delete_token is False:
        abort(404)
    else:
        return jsonify({}), 200
