import unittest

from tests.assignments import test_assign3

suite = unittest.TestLoader().loadTestsFromModule(test_assign3)
unittest.TextTestRunner(verbosity=2).run(suite)
