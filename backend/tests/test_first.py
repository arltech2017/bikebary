#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import unittest

__appname__     = "first"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

class MyTest(unittest.TestCase):
    def test(self):
        try:
            import flask
        except ImportError as e:
            self.fail("could not import flask: {}".format(e.msg))

if __name__ == '__main__':
    unittest.main()
