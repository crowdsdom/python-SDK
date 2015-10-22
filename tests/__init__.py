from __future__ import absolute_import
import unittest
import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))


def main():
    files = os.listdir(cwd)
    test_files = []
    for f in files:
        if f.startswith('test_') and f.endswith('.py'):
            test_files.append('tests.%s' % (f[0:-3]))
    suite = unittest.TestLoader().loadTestsFromNames(test_files)
    runner = unittest.TextTestRunner(verbosity=1 + sys.argv.count('-v'))
    raise SystemExit(not runner.run(suite).wasSuccessful())


if __name__ == '__main__':
    sys.path.insert(
        0, os.path.dirname(cwd)
    )
    main()
