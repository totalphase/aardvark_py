import unittest

# NOTE: unittest discovery should not be used because it tries to import all
# the modules in the package, including the extension modules that are are
# compiled for other systems / architectures.

# currently there are no tests, so just return an empty test suite
test_suite = unittest.TestSuite()
