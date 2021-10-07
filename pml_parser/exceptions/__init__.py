class BasePymlError(Exception):
    __module__ = Exception.__module__
class PymlSyntaxError(BasePymlError):
    pass    