#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.authorization_header({"": "Basic ianvoirnvo"}))
