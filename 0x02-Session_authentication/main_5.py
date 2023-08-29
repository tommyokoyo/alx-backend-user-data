#!/usr/bin/env python3
""" Main 4
"""

from api.v1.auth.session_auth import SessionAuth
from models.base import Base
base = Base()
existing_users = base.search({"email": "bobsession@hbtn.io"})
for user in existing_users:
    print(user)
print(type(existing_users))
