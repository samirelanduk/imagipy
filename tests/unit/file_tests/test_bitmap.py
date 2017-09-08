from unittest import TestCase
from imagipy.files.bitmap import split_bitmap

class SplitBitmapTests(TestCase):

    def test_can_split_bitmap(self):
        bmp_header = b"BMAAAAAAAA9\x00\x00\x00"
        dib_header = b"(\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        filler = b"FFF"
        pixels = b"RGBRGBRGBRGBRGBRGBRGB"
        data = bmp_header + dib_header + filler + pixels
        sections = split_bitmap(data)
        self.assertEqual(sections, [
         b"BMAAAAAAAA9\x00\x00\x00",
         b"(\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
         b"FFF",
         b"RGBRGBRGBRGBRGBRGBRGB"
        ])
