"""Tests for Versatuple."""

import unittest
from src.versatuple import versatuple

class TestVersatuple(unittest.TestCase):
    """Tests for Versatuple"""

    def test_versatuple_base_case(self):
        """In the base case, a versatuple should behave exactly as a namedtuple."""
        VTuple = versatuple("VTuple", ("id", "color", "direction", "count"))
        id_, color, direction, count = 3, "yellow", "n", 25
        vt = VTuple(id_, color, direction, count)
        self.assertEqual(vt.id, id_)
        self.assertEqual(vt.color, color)
        self.assertEqual(vt.direction, direction)
        self.assertEqual(vt.count, count)
