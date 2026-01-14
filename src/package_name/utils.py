from typing import Generic, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")


class dotdict(dict, Generic[_K, _V]):
    """
    A dictionary subclass that allows attribute access using dot notation.

    This provides a convenient way to access dictionary keys as if they were
    object attributes.

    Example
    -------
    >>> data = dotdict({'a': 1, 'b': 2})
    >>> data.a
    1
    >>> data.c = 3
    >>> data['c']
    3
    """

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key: _K) -> _V:
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'") from e
