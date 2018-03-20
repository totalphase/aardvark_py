Total Phase Aardvark Python API
===============================

.. image:: https://img.shields.io/pypi/v/aardvark-py.svg
    :alt: PyPI version
    :target: https://pypi.python.org/pypi/aardvark-py

.. image:: https://img.shields.io/pypi/pyversions/aardvark-py.svg
    :alt: Python versions
    :target: https://pypi.python.org/pypi/aardvark-py

.. image:: https://img.shields.io/readthedocs/aardvark_py.svg
    :alt: RTD build
    :target: https://aardvark-py.readthedocs.io/

.. image:: https://img.shields.io/github/tag/expressjs/express.svg
    :alt: GitHub tag
    :target: https://github.com/FlyingCampDesign/aardvark_py

This package provides the Total Phase Aardvark Python API packaged for easy
distribution and installation via PyPI.


Total Phase Release Versions
----------------------------

The "``major.minor``" component of the PyPI release version
(``major.minor.micro``) matches the ``v[major.minor]`` version of the aardvark
API release zip file.  For example, the ``aardvark-py 5.15.0`` release on PyPI
is guaranteed to be API compatible with
``aardvark-api-[platform]-[arch]-v5.15.zip``.  The "``micro``" component is an
additional version specifier that is incremented whenever a new release of this
package is published on PyPI.


OS Support
----------

The Python API from Total Phase officially supports the following OS versions:

- Windows 7, 8, 8.1, 10
- Mac OS 10.5 - 10.12
- Ubuntu 12.04 LTS, 14.04 LTS, 16.04 LTS

Since this package is derived directly from Total Phase API releases, it is
subject to the same compatibility restrictions.


Python 3 Support
----------------

API version 5.30 adds support for Python 3 (previous versions only supported
Python 2).


Installation
------------

The ``aardvark_py`` package can be installed from PyPI using ``pip``:

.. code-block:: console

    $ pip install aardvark_py


Usage
-----

Once installed, the ``aardvark_py`` package is a drop-in replacement for the
``aardvark_py.py`` language module distributed in the Aardvark API release from
Total Phase.

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


Development
-----------

.. code-block:: console

    $ git clone https://github.com/FlyingCampDesign/aardvark_py.git
    $ cd aardvark_py
    $ make dev-install
    $ make

Open ``docs/_build/html/index.html`` in a browser to view the generated
documentation.


License
-------

Permission to modify and redistribute the Python language modules and associated
shared object files has been granted explicitly by Total Phase, Inc. for use in
this package.  Distribution and use of this package is subject to the license
agreement provided in the ``LICENSE.txt`` file distributed with this package.


.. _Python.org: http://www.python.org
.. _Pipenv: https://docs.pipenv.org
.. _`officially recommended`: https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies