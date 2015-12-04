"""TotalPhase Aardvark Python API.

See:
http://www.totalphase.com/products/aardvark-software-api
"""

import os, re, codecs

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# from https://github.com/pypa/pip/blob/develop/setup.py
def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()

# from https://github.com/pypa/pip/blob/develop/setup.py
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    # https://www.python.org/dev/peps/pep-0426/#name
    name='aardvark_py',

    # Extract version string from module
    version=find_version('aardvark_py', '__init__.py'),

    description="TotalPhase Aardvark Python API",
    long_description=read('README.rst'),

    # The project's main homepage
    url='https://github.com/FlyingCampDesign/aardvark_py.git',

    # Author details
    author='Flying Camp Design',
    author_email='support@flyingcampdesign.com',

    # Choose your license
    license='Proprietary License (see LICENSE.txt provided with the distribution)',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: Other/Proprietary License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'tests']),

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'aardvark_py': ['aardvark.so', 'aardvark.dll'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('', ['LICENSE.txt'])],
)
