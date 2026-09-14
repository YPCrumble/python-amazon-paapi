"""Unit tests for the timeout values accepted by the clients."""

from __future__ import annotations

import unittest

from amazon_creatorsapi.core.timeouts import UNSET


class TestUnset(unittest.TestCase):
    """Tests for the sentinel of an argument that was not given."""

    def test_is_falsy(self) -> None:
        """Test that the sentinel reads as absent."""
        self.assertFalse(UNSET)

    def test_repr_names_it(self) -> None:
        """Test that the sentinel is readable in a signature."""
        self.assertEqual(repr(UNSET), "UNSET")
