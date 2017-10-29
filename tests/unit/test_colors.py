from unittest import TestCase
from unittest.mock import Mock, patch
from imagipy.colors import Color

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



class RandomColorTests(TestCase):

    @patch("imagipy.colors.randint")
    def test_can_get_random_color(self, mock_rand):
        mock_rand.side_effect = [23, 45, 67]
        color = Color.random()
        mock_rand.assert_called_with(0, 255)
        self.assertEqual(mock_rand.call_count, 3)
        self.assertEqual(color._r, 23)
        self.assertEqual(color._g, 45)
        self.assertEqual(color._b, 67)



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



class ColorMutationTests(TestCase):

    @patch("imagipy.colors.randint")
    def test_can_mutate_color(self, mock_rand):
        mock_rand.side_effect = [23, 45, 67]
        color = Color(24, 149, 134)
        new_color = color.mutate()
        mock_rand.assert_any_call(8, 40)
        mock_rand.assert_any_call(133, 165)
        mock_rand.assert_any_call(118, 150)
        self.assertEqual(new_color._r, 23)
        self.assertEqual(new_color._g, 45)
        self.assertEqual(new_color._b, 67)


    @patch("imagipy.colors.randint")
    def test_color_mutation_doesnt_stray_beyond_bounds(self, mock_rand):
        mock_rand.side_effect = [-4, 258, 0]
        color = Color(24, 149, 134)
        new_color = color.mutate()
        mock_rand.assert_any_call(8, 40)
        mock_rand.assert_any_call(133, 165)
        mock_rand.assert_any_call(118, 150)
        self.assertEqual(new_color._r, 0)
        self.assertEqual(new_color._g, 255)
        self.assertEqual(new_color._b, 0)
