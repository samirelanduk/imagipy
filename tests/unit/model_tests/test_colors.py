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



class ColorFromHexTests(TestCase):

    def test_can_get_color_from_hex(self):
        color = Color.from_hex("#0B9586")
        self.assertEqual(color._r, 11)
        self.assertEqual(color._g, 149)
        self.assertEqual(color._b, 134)


    def test_can_get_color_from_hex_without_hash(self):
        color = Color.from_hex("0B9586")
        self.assertEqual(color._r, 11)
        self.assertEqual(color._g, 149)
        self.assertEqual(color._b, 134)


    def test_hex_must_be_str(self):
        with self.assertRaises(TypeError):
            Color.from_hex(123)


    def test_hex_must_be_valid(self):
        with self.assertRaises(ValueError):
            Color.from_hex("0B986")
        with self.assertRaises(ValueError):
            Color.from_hex("#0B986")
        with self.assertRaises(ValueError):
            Color.from_hex("")



class ColorReprTests(TestCase):

    def test_can_get_color_repr(self):
        color = Color(74, 149, 134)
        self.assertEqual(str(color), "<Color (74, 149, 134)>")



class ColorRgbTests(TestCase):

    def test_can_get_color_rgb(self):
        color = Color(74, 149, 134)
        self.assertEqual(color.rgb(), (74, 149, 134))



class ColorHexTests(TestCase):

    def test_can_get_color_as_hex(self):
        color = Color(11, 149, 134)
        self.assertEqual(color.hex(), "#0B9586")
