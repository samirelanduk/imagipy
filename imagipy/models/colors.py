"""This module contains classes and functions for processing colors."""

from random import randint

class Color:
    """Represents a color.

    :param int r: The Red value (0-255).
    :param int g: The Green value (0-255).
    :param int b: The Blue value (0-255).
    :raises TypeError: if a non-int RGB value is given.
    :raises ValueError: if an RGB value outside 0-255 is given."""

    def __init__(self, r, g, b):
        for rgb in (r, g, b):
            if not isinstance(rgb, int):
                raise TypeError("RGB value {} is not int".format(rgb))
            if rgb < 0 or rgb > 255:
                raise ValueError("RGB value {} not within 0-255".format(rgb))
        self._r, self._g, self._b = r, g, b


    @staticmethod
    def from_hex(hexcolor):
        """An alternate constructor which creates a color from a hex string
        such as ``'#0B9586'``. The preceding `#` is optional.

        :param str hexcolor: The hex string representing the desired color.
        :raises TypeError: if a non-string is given.
        :raises ValueError: if the hex string is not valid.
        :rtype: ``Color``"""

        if not isinstance(hexcolor, str):
            raise TypeError("{} is not a string".format(hexcolor))
        if hexcolor and hexcolor[0] == "#":
            hexcolor = hexcolor[1:]
        try:
            if len(hexcolor) != 6: raise ValueError
            rgb = [int(hexcolor[i * 2:i * 2 + 2], 16) for i in range(3)]
            return Color(*rgb)
        except:
            raise ValueError("{} is not a valid hex color".format(hexcolor))


    @staticmethod
    def random():
        """An alternate constructor which creates a random color

        :rtype: ``Color``"""
        
        return Color(randint(0, 255), randint(0, 255), randint(0, 255))


    def __repr__(self):
        return "<Color ({}, {}, {})>".format(self._r, self._g, self._b)


    def rgb(self):
        """Returns the color's RGB values.

        :rtype: ``tuple``"""

        return (self._r, self._g, self._b)


    def hex(self):
        """Returns the color as a hex string (#RRGGBB)

        :rtype: ``str``"""

        return "#{:02X}{:02X}{:02X}".format(self._r, self._g, self._b)
