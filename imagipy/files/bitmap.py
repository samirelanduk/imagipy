"""Contains functions and classes for handling bitmap files."""

import struct

def split_bitmap(data):
    """Splits the bytes of a bitmap file into four sections: file header, image
    header, color table, and pixel data.

    :param bytes data: The bitmap file data.
    :rtype: ``list``"""

    file_header = data[:14]
    dib_length = struct.unpack("i", data[14:18])[0]
    image_header = data[14:14 + dib_length]
    pixel_offset = struct.unpack("i", data[10:14])[0]
    pixels = data[pixel_offset:]
    color_table = data[14 + dib_length:pixel_offset]
    return [file_header, image_header, color_table, pixels]


def header_to_dict(header):
    """Takes the bytes of a bitmap image header and creates a ``dict`` of its
    key information.

    :param bytes header: a bitmap image header.
    :rtype: ``dict``"""

    return {
     "width": struct.unpack("i", header[4:8])[0],
     "height": struct.unpack("i", header[8:12])[0],
     "bits_per_pixel": struct.unpack("h", header[14:16])[0],
     "compression": struct.unpack("i", header[16:20])[0],
     "size_image": struct.unpack("i", header[20:24])[0],
     "x_per_meter": struct.unpack("i", header[24:28])[0],
     "y_per_meter": struct.unpack("i", header[28:32])[0],
     "color_used": struct.unpack("i", header[32:36])[0],
     "color_important": struct.unpack("i", header[36:40])[0]
    }
