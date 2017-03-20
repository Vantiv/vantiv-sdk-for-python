# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

def run_tests(_test_dirs):
    import os
    import re
    import sys
    import unittest
    import types

    dirs = _test_dirs
    tests = []

    # regex for unittest sources
    _testfile_re = re.compile('^test.*\.py$')

    # build test file list.
    while dirs:
        package_root = os.path.abspath(os.path.dirname(__file__))
        d = os.path.join(package_root, dirs.pop(0))
        for f in os.listdir(d):
            fn = os.path.join(d, f)
            if os.path.isdir(fn):
                dirs.append(fn)
            if _testfile_re.match(f):
                tests.append(fn)

    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    test_names = set()

    # Learn from https://github.com/pabigot/pyxb/blob/next/setup.py
    for fn in tests:
        try:
            # Assign a unique name for this test
            test_name = os.path.basename(fn).split('.')[0]
            test_name = test_name.replace('-', '_')
            number = 2
            base_name = test_name
            while test_name in test_names:
                test_name = '%s%d' % (base_name, number)
                number += 1
            # Read the test source in and compile it
            rv = compile(open(fn).read(), test_name, 'exec')

            # Make a copy of the globals array so we don't
            # contaminate this environment.
            g = globals().copy()

            # The test cases use __file__ to determine the path to
            # the schemas
            g['__file__'] = fn

            # Create a module into which the test will be evaluated.
            module = types.ModuleType(test_name)

            # The generated code uses __name__ to look up the
            # containing module in sys.modules.
            g['__name__'] = test_name
            sys.modules[test_name] = module

            # Import the test into the module, making sure the created globals look like they're in the module.
            eval(rv, g)
            module.__dict__.update(g)

            # Find all subclasses of unittest.TestCase that were
            # in the test source and add them to the suite.
            for (nm, obj) in g.items():
                if (type == type(obj)) and issubclass(obj, unittest.TestCase):
                    suite.addTest(loader.loadTestsFromTestCase(obj))
        except Exception as e:
            raise

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
