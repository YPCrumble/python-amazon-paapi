"""Timeout values accepted by the clients.

A timeout is either a number of seconds covering the whole request, or a pair
of ``(connect, read)`` seconds covering each leg on its own. The pair matters
for a host that resolves to several addresses: the connect leg is spent once
per address, so a single value generous enough to read a slow response is
also spent on every address that fails to answer.
"""

from __future__ import annotations

from typing import Final, Union

TimeoutValue = Union[float, "tuple[float, float]"]
"""Seconds for the whole request, or ``(connect, read)`` seconds per leg."""


class UnsetType:
    """Type of the sentinel meaning that an argument was not given.

    A timeout of ``None`` means waiting indefinitely, so it cannot double as
    "not given". This sentinel keeps the two apart.
    """

    def __repr__(self) -> str:
        """Return the representation used in signatures and errors."""
        return "UNSET"

    def __bool__(self) -> bool:
        """Return False, so the sentinel reads as absent."""
        return False


UNSET: Final = UnsetType()
"""Sentinel for an argument that was not given."""
