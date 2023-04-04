"""Tests for Versatuple."""
# pylint: disable=invalid-name

import unittest
from src.versatuple import versatuple

class TestVersatuple(unittest.TestCase):
    """Tests for Versatuple"""

    def test_base_case(self):
        """Test basic functionality."""
        VTuple = versatuple("VTuple", ("id", "color", "direction", "count"))
        id_, color, direction, count = 3, "yellow", "n", 25
        vt = VTuple.new().with_id(id_).with_color(color).with_direction(direction).with_count(count)
        self.assertEqual(vt.id, id_)
        self.assertEqual(vt.color, color)
        self.assertEqual(vt.direction, direction)
        self.assertEqual(vt.count, count)
        vt2 = VTuple(id_, color, direction, count)
        self.assertEqual(vt, vt2)

    def test_defaults(self):
        """If defaults are supplied, they should be set."""
        VTuple = versatuple("VTuple",
                            ("id", "color", "direction", "count"),
                            defaults=(33, "red", "n", 222))
        vt = VTuple.new()
        self.assertEqual(vt, (33, "red", "n", 222))


    def test_immutable_setters(self):
        """Immutable Setters should exist and work correctly."""
        VTuple = versatuple("VTuple", ("id", "color", "direction", "count"))
        vt = VTuple(3, "yellow", "north", 25)
        vt2 = vt.with_id(4)
        self.assertEqual(vt2, (4, "yellow", "north", 25))
        vt3 = vt2.with_color("green")
        self.assertEqual(vt3, (4, "green", "north", 25))
        vt4 = vt3.with_direction("south")
        self.assertEqual(vt4, (4, "green", "south", 25))
        vt5 = vt4.with_count(300)
        self.assertEqual(vt5, (4, "green", "south", 300))

    def test_is_valid(self):
        """Test validation of versatuple."""
        validators = {"color": lambda _color: _color in ("yellow", "red"),
                      "count": lambda _count: 0 <= _count < 100}
        VTuple = versatuple("VTuple", ("id", "color", "direction", "count"),
                            field_validators_dict=validators)
        id_, color, direction, count = 3, "yellow", "n", 25
        vt = VTuple(id_, color, direction, count)
        self.assertTrue(vt.is_valid())
        self.assertFalse(vt.with_color("green").is_valid())
        self.assertFalse(vt.with_count(-1).is_valid())
        self.assertFalse(vt.with_count(100).is_valid())

    def test_field_shortcuts(self):
        """Test field shortcuts of versatuple."""
        shortcuts = (("color", "yellow", "yellow"), ("color", "red", "red"), ("count", "count1", 1))
        VTuple = versatuple("VTuple",
                            ("id", "color", "direction", "count"),
                            field_shortcuts=shortcuts)
        id_, color, direction, count = 3, "blue", "n", 25
        vt = VTuple(id_, color, direction, count)
        vt2 = vt.yellow()
        self.assertEqual(vt2.color, "yellow")
        vt3 = vt.red()
        self.assertEqual(vt3.color, "red")
        vt4 = vt.count1()
        self.assertEqual(vt4.count, 1)
