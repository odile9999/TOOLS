#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""

tests.test_files Created on 18 dec. 2017
"""
import os
import tempfile
import unittest

from src.files import PireneaFiles


class PireneaFilesTestCase(unittest.TestCase):

    def setUp(self):
        """Called before test case."""
        self.bad_prefix = "P3"
        self.nonexist = "trugludu"

    def test_check_input(self):
        """Wrong directory."""
        with self.assertRaises(ValueError):
            with tempfile.TemporaryDirectory() as bad_tmpdirname:
                self.pirenea = PireneaFiles(bad_tmpdirname)
        """Nonexistent directory."""
        with self.assertRaises(ValueError):
            self.pirenea = PireneaFiles(self.nonexist)
        """Wrong prefix."""
        with tempfile.TemporaryDirectory(prefix="PIRENEA_DATA") as tmpdirname:
            self.pirenea = PireneaFiles(tmpdirname)
            with self.assertRaises(ValueError):
                self.pirenea.add_prefix(self.bad_prefix)

    def test_add_remove_prefix(self):
        with tempfile.TemporaryDirectory(prefix="PIRENEA_DATA") as tmpdirname:
            with tempfile.TemporaryFile(dir=tmpdirname) as tf:
                self.pirenea = PireneaFiles(tmpdirname)
                self.pirenea.add_prefix("P0")
                self.pirenea.remove_prefix("P0")
                """Check if temporary file tf is unchanged"""
                self.assertTrue(os.path.isfile(tf.name))


if __name__ == "__main__":
    unittest.main()
