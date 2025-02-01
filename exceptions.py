# exceptions.py
class InvalidDimensionError(ValueError):
    """Raised when a dimension (e.g., radius) is non-positive."""
