Overview
--------

imagipy is an image processing library. It currently has tools for dealing with
colors.

Colors
~~~~~~

Colors are created with the :py:class:`.Color` class:

  >>> import imagipy
  >>> purple = imagipy.Color(255, 0, 255)
  >>> purple
  <Color (255, 0, 255)>

You can also create colors from hex strings:

  >>> orange = imagipy.Color.from_hex("#E67E22")
  >>> orange
  <Color (230, 126, 34)>

imagipy comes with some pre-set colors:

  >>> imagipy.Color.YELLOW
  <Color (241, 196, 15)>
  >>> imagipy.Color.GRAY
  <Color (204, 204, 204)>
  >>> imagipy.Color.BROWN
  <Color (124, 63, 0)>

You can get a random color, or mutate an existing color to get a slight variant
on it:

  >>> imagipy.Color.random()
  <Color (45, 217, 230)>
  >>> imagipy.Color.random()
  <Color (249, 244, 177)>
  >>> imagipy.Color.random()
  <Color (112, 178, 218)>
  >>> orange.mutate()
  <Color (229, 131, 43)>
  >>> orange.mutate()
  <Color (216, 127, 28)>
  >>> orange.mutate()
  <Color (235, 127, 29)>

Colors can be converted to RGB or hex:

  >>> orange.rgb()
  (230, 126, 34)
  >>> orange.hex()
  '#E67E22'
