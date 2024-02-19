#!/usr/bin/python3
# 2-is_same_class.py
# [Your Name] <[Your Email]>

"""
Defines a function for checking if an object is exactly an instance of a given class.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
