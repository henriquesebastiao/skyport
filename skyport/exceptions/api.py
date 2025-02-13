"""Exceptions raised during errors when consuming third-party APIs."""


class ApiKeyInvalid(Exception):
    pass


class ApiKeyLimitExceeded(Exception):
    pass


class IncompatibleParameterFormat(Exception):
    pass


class ItemNotFound(Exception):
    pass
