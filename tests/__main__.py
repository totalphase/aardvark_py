import unittest
from tests import test_suite

# use the basic test runner that outputs to sys.stderr
test_runner = unittest.TextTestRunner()

# run the test suite
test_runner.run(test_suite)
