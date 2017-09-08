"""Contains functions and classes for handling bitmap files."""

import struct

def split_bitmap(data):
    """Splits the bytes of a bitmap file into four sections: file header, image
    header, color table, and pixel data.

    :param bytes data: The bitmap file data.
    :rtype: ``list``"""

    file_header = data[:14]
    dib_length = struct.unpack("I", data[14:18])[0]
    image_header = data[14:14 + dib_length]
    pixel_offset = struct.unpack("I", data[10:14])[0]
    pixels = data[pixel_offset:]
    color_table = data[14 + dib_length:pixel_offset]
    return [file_header, image_header, color_table, pixels]
