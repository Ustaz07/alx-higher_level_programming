def is_same_class(obj, a_class):
    """
    Check if the given object is an exact instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class; otherwise, returns False.
    """
    return type(obj) is a_class
