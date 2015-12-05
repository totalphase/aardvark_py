Total Phase Aardvark Python API
===============================

This package provides the Total Phase Aardvark Python API modified for easy
distribution and installation via PyPI.


Compatibility
-------------

The "``major.minor``" component of the PyPI release version
(``major.minor.micro``) matches the ``v[major.minor]`` version of the aardvark
API release zip file.  For example, the ``aardvark-py 5.15.0`` release on PyPI
is guaranteed to be API compatible with
``aardvark-api-[platform]-[arch]-v5.15.zip``.  The "``micro``" component is an
additional version specifier that is incremented whenever a new release of this
package is published.

The Python API from Total Phase currently only supports Mac OS X, Linux, and
Windows (32-bit & 64-bit).  Since this package is derived directly from Total
Phase API releases, it is subject to the same compatibility restrictions.


Installation
------------

The ``aardvark_py`` package can be installed from PyPI using ``pip``:

.. code-block:: console

    $ pip install aardvark_py


Usage
-----

Once installed, the ``aardvark_py`` package is a drop-in replacement for the
``aardvark_py.py`` language module distributed in the Aardvark API release.

.. code-block:: console

    $ python
    Python 2.7.10 (default, Dec  3 2015, 13:28:10)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from aardvark_py import *
    >>> aa_find_devices(1)
    (1, array('H', [0]))
    >>> handle = aa_open(0)
    >>> aa_features(handle)
    27
    >>> aa_close(handle)
    1


License
-------

Permission to modify and redistribute the Python language modules and associated
shared object files has been granted explicitly by Total Phase, Inc. for use in
this package.  Distribution and use of this package is subject to the license
agreement provided in the LICENSE.txt file distributed with this package.
