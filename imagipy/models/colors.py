"""This module contains classes and functions for processing colors."""

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
