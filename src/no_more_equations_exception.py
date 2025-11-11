class NoMoreEquationsException(Exception):
    """
    Raised when the equation can't be parsed,
    assuming that the file is in proper format,
    that means A = {action_1, action_2, ..., action_n} is read,
    so another line is w = [action_1, action_2, ..., action_n]+.
    """
    pass