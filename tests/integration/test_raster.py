from unittest import TestCase
import imagipy

class BmpTests(TestCase):

    def test_can_open_monochrome_bitmap(self):
        image = imagipy.open("tests/integration/files/monochrome.bmp")

        self.assertEqual(image.width(), 20)
        self.assertEqual(image.height(), 10)

        grid = image.grid()
        self.assertEqual(grid[0][0].hex(), "#000000")
        self.assertEqual(grid[0][10].hex(), "#FFFFFF")
        self.assertEqual(grid[-1][-1].hex(), "#000000")
