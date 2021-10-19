class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
