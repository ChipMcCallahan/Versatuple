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
        vt = VTuple.new().Id(id_).Color(color).Direction(direction).Count(count)
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
        vt2 = vt.Id(4)
        self.assertEqual(vt2, (4, "yellow", "north", 25))
        vt3 = vt2.Color("green")
        self.assertEqual(vt3, (4, "green", "north", 25))
        vt4 = vt3.Direction("south")
        self.assertEqual(vt4, (4, "green", "south", 25))
        vt5 = vt4.Count(300)
        self.assertEqual(vt5, (4, "green", "south", 300))

    def test_is_valid(self):
        """Test validation of versatuple."""
        validators = {"color": lambda _color: _color in ("yellow", "red"),
                      "count": lambda _count: 0 <= _count < 100}
        VTuple = versatuple("VTuple", ("id", "color", "direction", "count"),
                            validators=validators)
        id_, color, direction, count = 3, "yellow", "n", 25
        vt = VTuple(id_, color, direction, count)
        self.assertTrue(vt.is_valid())
        self.assertFalse(vt.Color("green").is_valid())
        self.assertFalse(vt.Count(-1).is_valid())
        self.assertFalse(vt.Count(100).is_valid())

    def test_field_shortcuts(self):
        """Test field shortcuts of versatuple."""
        shortcuts = {"color": [("yellow", "yellow"), ("red", "red")],
                     "count": [("count1", 1)]}
        VTuple = versatuple("VTuple",
                            ("id", "color", "direction", "count"),
                            shortcuts=shortcuts)
        id_, color, direction, count = 3, "blue", "n", 25
        vt = VTuple(id_, color, direction, count)
        vt2 = vt.yellow()
        self.assertEqual(vt2.color, "yellow")
        vt3 = vt.red()
        self.assertEqual(vt3.color, "red")
        vt4 = vt.count1()
        self.assertEqual(vt4.count, 1)

    def test_factories(self):
        """Test factories of versatuple."""
        factories = {
            "yellow_south_3": {"color": "yellow", "direction": "s", "count": 3},
            "blue_99": {"color": "blue", "count": 99},
            "id_22": {"id": 22}
        }
        VTuple = versatuple("VTuple",
                            ("id", "color", "direction", "count"),
                            defaults=(33, "red", "n", 222),
                            factories=factories)
        self.assertEqual(VTuple.yellow_south_3(), (33, "yellow", "s", 3))
        self.assertEqual(VTuple.blue_99(), (33, "blue", "n", 99))
        self.assertEqual(VTuple.id_22(), (22, "red", "n", 222))
