# Reverse function that can handle many iterable types
# such as list, tuple, string, set and generator.
# Note: if set is given it returns a list as order is meaningless in sets.

from collections.abc import Iterable


def reverse(iterable: Iterable):
    if isinstance(iterable, range) or isinstance(iterable, set):
        return list(iterable)[::-1]
    return iterable[::-1]
