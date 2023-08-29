"""
    Regixing
"""
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    """
        Returns an obfuscated Log message
        :arg
            fields - list of strings representing all fields to obfuscate
            redaction - string representing by what the field will be obfuscated
            message - string representing the log line
            separator - string representing by which character is
                        separating all fields in the log line
        :return: Log message
    """
    pass
