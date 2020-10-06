"""
Library-wise errors
"""


class ConnectorXError(Exception):
    """
    Base exception, used library-wise
    """


class UnreachableError(ConnectorXError):
    """
    Error indicating some path of the code is unreachable.
    """
