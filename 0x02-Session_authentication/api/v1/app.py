#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv('AUTH_TYPE', 'basic_auth')
if AUTH_TYPE == 'auth':
     from api.v1.auth.auth import Auth
     auth = Auth()
elif AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
        Request unauthorized handler
        Args:
            error:

        Returns: JSON{"error:Unauthorized"}
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
        Request forbidden handler
        Args:
            error:

        Returns: JSON{"error:Forbidden"}
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """
        Request unauthorized handler
        Args:
            error:

        Returns: JSON{"error:Not found"}
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request() -> str:
    """
        Executed before a request is handled
    """
    ex_path = ['/api/v1/status/', '/api/v1/unauthorized/',
               '/api/v1/forbidden/']
    if auth is None:
        return
    elif not auth.require_auth(request.path, ex_path):
        return
    elif auth.authorization_header(request) is None:
        abort(401)
    elif auth.current_user(request) is None:
        abort(403)
    else:
        request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
