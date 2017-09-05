from unittest import TestCase
from imagipy.models.colors import Color

class ColorCreationTests(TestCase):

    def test_can_create_color(self):
        color = Color(74, 149, 134)
        self.assertEqual(color._r, 74)
        self.assertEqual(color._g, 149)
        self.assertEqual(color._b, 134)


    def test_color_needs_integers(self):
        with self.assertRaises(TypeError):
            Color(74, 149, 134.5)


    def test_color_needs_integers_in_correct_range(self):
        with self.assertRaises(ValueError):
            Color(74, 149, -1)
        with self.assertRaises(ValueError):
            Color(74, 149, 256)
