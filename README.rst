Total Phase Aardvark Python API
===============================

Official packages are available on PyPI.

https://pypi.org/project/aardvark-py/


The packages are created from the Aardvark API release package.

https://www.totalphase.com/products/aardvark-software-api


System Requirements
-------------------

- Windows 7 or 10
- Ubuntu 16.04 LTS or 18.04 LTS
- Mac OS 10.13+
- Python 2.6+ or 3.5+
- 64-bit operating system


Installation
------------

The ``aardvark_py`` package can be installed from PyPI using ``pip``:

.. code-block:: console

    $ pip3 install aardvark_py


Usage
-----

Once installed, the ``aardvark_py`` package is a drop-in replacement for the
``aardvark_py.py`` module distributed in the Aardvark API release package.

.. code-block:: console

    $ python3
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

Please see the LICENSE.txt file in the package.
