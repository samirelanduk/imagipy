"""Contains functions and classes for handling bitmap files."""

import struct

def split_bitmap(data):
    """Splits the bytes of a bitmap file into the two headers and pixel array.

    :param bytes data: The bitmap file data.
    :rtype: ``list``"""

    bmp_header = data[:14]
    dib_length = struct.unpack("I", data[14:18])[0]
    dib_header = data[14:14 + dib_length]
    pixel_offset = struct.unpack("I", data[10:14])[0]
    pixels = data[pixel_offset:]
    return [bmp_header, dib_header, pixels]
