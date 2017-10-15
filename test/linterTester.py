"""Linter class tester.

Author: Israel Blancas @iblancasa

License:
The MIT License (MIT)
    Copyright (c) 2015-2017 Israel Blancas @iblancasa (http://iblancasa.com/)
    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the Software), to deal in the Software
    without restriction, including without
    limitation the rights to use, copy, modify, merge,
    publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
    OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
    USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import unittest
from sys import path as sysPath
from os import path as osPath
try:
    from yacl import linter
except ImportError:
    filepath = osPath.dirname(osPath.realpath(__file__))
    sysPath.append(filepath + "/../")
    from yacl import linter


class LineCheckersTester(unittest.TestCase):
    """Tests for `linecheckers.py`."""

    def test_parsePragma(self):
        """Test the pragma parser."""
        # Given
        linterTest = linter.YACL()
        pragmaLine = "# yacl: disable=S001,S002"
        expectedOutput = ["S001", "S002"]

        # When
        # pylint: disable=W0212
        linterTest._YACL__parsePragma(pragmaLine)

        # Then
        self.assertEqual(linterTest.lineOptions["rules"]["oneLineIgnores"],
                         expectedOutput)


if __name__ == '__main__':
    unittest.main()
