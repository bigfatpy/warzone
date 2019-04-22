import os
import sys
import unittest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
tests_dir = os.path.dirname(os.path.abspath(__file__))
suite.addTests(loader.discover(start_dir=tests_dir))
runner = unittest.TextTestRunner(failfast=False, verbosity=2)
result = runner.run(suite)
if result.failures or result.errors:
    sys.exit(1)
