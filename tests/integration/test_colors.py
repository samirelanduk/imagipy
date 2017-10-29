from unittest import TestCase
from imagipy import Color

class ColorTests(TestCase):

    def test_colors(self):
        red = Color(255, 0, 0)
        green = Color.from_hex("#00FF00")
        blue = Color.from_hex("0000FF")

        self.assertEqual(red.rgb(), (255, 0, 0))
        self.assertEqual(green.rgb(), (0, 255, 0))
        self.assertEqual(blue.rgb(), (0, 0, 255))

        self.assertEqual(red.hex(), "#FF0000")
        self.assertEqual(green.hex(), "#00FF00")
        self.assertEqual(blue.hex(), "#0000FF")

        random = Color.random()
        for value in random.rgb():
            self.assertTrue(0 <= value <= 255)

        for _ in range(100):
            new_random = random.mutate()
            self.assertNotEqual(random.rgb(), new_random.rgb())
            for value in new_random.rgb():
                self.assertTrue(0 <= value <= 255)
            random = new_random
