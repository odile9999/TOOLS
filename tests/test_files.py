#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""

tests.test_files Created on 18 dec. 2017
"""

import unittest

from src.files import PireneaFiles


class PireneaFilesTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.pirenea = PireneaFiles()
        self.folder = "D:/PIRENEA/DATA_1"
        self.bad_folder = "c:/documents"
        self.empty = ""

    def test_add_prefix(self):
        with self.assertRaises(ValueError):
            self.pirenea.__init__(self.bad_folder)
        with self.assertRaises(ValueError):
            self.pirenea.__init__(self.empty)
        with self.assertRaises(ValueError):
            self.pirenea.__init__(self.folder)
            self.pirenea.add_prefix("PO")

    def test_remove_prefix(self):
        with self.assertRaises(ValueError):
            self.pirenea.__init__(self.folder)
            self.pirenea.remove_prefix(self.empty)

if __name__ == "__main__":
    unittest.main()
