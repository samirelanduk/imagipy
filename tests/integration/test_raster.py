from unittest import TestCase
import imagipy

class BmpTests(TestCase):

    def test_can_open_bitmap(self):
        image = imagipy.open("tests/integration/files/simple.bmp")

        self.assertEqual(image.width(), 200)
        self.assertEqual(image.height(), 150)

        grid = image.grid()
        self.assertEqual(grid[0][0].hex(), "#FF0000")
        self.assertEqual(grid[-1][-1].hex(), "#0000FF")
