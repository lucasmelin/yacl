"""One line checkers tester.

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
    from yacl import linecheckers
except ImportError:
    filepath = osPath.dirname(osPath.realpath(__file__))
    sysPath.append(filepath + "/../")
    from yacl import linecheckers


class LineCheckersTester(unittest.TestCase):
    """Tests for `linecheckers.py`."""

    def test_checkLineLength(self):
        """Check if the length of one line is the expected one."""
        # Given
        options = {
            "lineLength": 80
        }
        lineToTest1 = "a"*25
        lineToTest2 = "a"*90

        # When
        result1 = linecheckers.checkLineLength(lineToTest1, options)
        result2 = linecheckers.checkLineLength(lineToTest2, options)

        # Then
        self.assertEqual(result1, "")
        self.assertEqual(result2, "Length of the line is more than 80 (90)")


if __name__ == '__main__':
    unittest.main()