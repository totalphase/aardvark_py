TotalPhase Aardvark Python API
==============================

This package provides the TotalPhase Aardvark Python API modified for easy
distribution and installation via PyPI.


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
