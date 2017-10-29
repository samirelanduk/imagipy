.. |travis| image:: https://api.travis-ci.org/samirelanduk/imagipy.svg?branch=0.1

.. |coveralls| image:: https://coveralls.io/repos/github/samirelanduk/imagipy/badge.svg?branch=0.1

.. |pypi| image:: https://img.shields.io/pypi/pyversions/imagipy.svg


|travis| |coveralls| |pypi|

imagipy
=======

imagipy is an image and color processing library.

Example
-------

  >>> import imagipy
  >>> red = Color(255, 0, 0)
  >>> green = Color.from_hex("#00FF00")
  >>> blue = Color.from_hex("0000FF")
  >>> red.mutate()
  <Color (249, 2, 7)>





Installing
----------

pip
~~~

imagipy can be installed using pip:

``$ pip3 install imagipy``

imagipy is written for Python 3, and does not support Python 2. It is currently
tested on Python 3.5 and above.

If you get permission errors, try using ``sudo``:

``$ sudo pip3 install imagipy``


Development
~~~~~~~~~~~

The repository for imagipy, containing the most recent iteration, can be
found `here <http://github.com/samirelanduk/imagipy/>`_. To clone the
imagipy repository directly from there, use:

``$ git clone git://github.com/samirelanduk/imagipy.git``


Requirements
~~~~~~~~~~~~

imagipy currently has no dependencies.


Overview
--------

imagipy is an image processing library. It currently has tools for dealing with
colors.

Colors
~~~~~~

Colors are created with the ``Color`` class:

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


Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`29 October 2017`

* Added basic Color class.
* Added Color generation from RGB, hex, random, and mutation.
