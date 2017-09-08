from unittest import TestCase
from imagipy.files.bitmap import split_bitmap, header_to_dict

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



class ImageHeaderToDictTests(TestCase):

    def test_can_turn_image_header_into_dict(self):
        header = (b"(\x00\x00\x00\xc8\x00\x00\x00j\xff\xff\xff" +
        b"\x01\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" +
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        self.assertEqual(header_to_dict(header), {
         "width": 200,
         "height": -150,
         "bits_per_pixel": 32,
         "compression": 0,
         "size_image": 0,
         "x_per_meter": 0,
         "y_per_meter": 0,
         "color_used": 0,
         "color_important": 0
        })
