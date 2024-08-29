#!/usr/bin/env python3
"""Module for password encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted and hashed password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates that the password matches the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
