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
        ignoreOption = {
            "rules": {
                "oneLineIgnores": ["S001"]
            }
        }
        options = {
            "lineLength": 80
        }
        shortLine = "a"*25
        longLine = "a"*90

        # When
        resultIgnore = linecheckers.checkLineLength(shortLine, ignoreOption)

        noError = linecheckers.checkLineLength(shortLine, options)
        errorLong = linecheckers.checkLineLength(longLine, options)

        # Then
        self.assertEqual(resultIgnore, "")
        self.assertEqual(noError, "")
        self.assertEqual(errorLong, "Length of the line is more than 80 (90)")

    def test_checkCommandUpperLowerCaseUPPER(self):
        """Check if the commands are in UPPER case."""
        # Given
        ignoreOption = {
            "rules": {
                "oneLineIgnores": ["S002"]
            }
        }
        optionsUpper = {
            "commandsStyle": "uppercase"
        }

        upperCommand = "FIND_PACKAGE()"
        lowerCommand = "find_package()"
        mixedCommand = "FiNd_PaCkAgE()"
        noCommand = "\"OpenSSL\""

        # When
        resultIgnore = linecheckers.checkCommandUpperLowerCase(upperCommand,
                                                               ignoreOption)
        noErrorCommand = linecheckers.checkCommandUpperLowerCase(noCommand,
                                                                 optionsUpper)

        noErrorUpper = linecheckers.checkCommandUpperLowerCase(upperCommand,
                                                               optionsUpper)
        lowerErrorU = linecheckers.checkCommandUpperLowerCase(lowerCommand,
                                                              optionsUpper)
        mixedErrorU = linecheckers.checkCommandUpperLowerCase(mixedCommand,
                                                              optionsUpper)

        # Then
        self.assertEqual(resultIgnore, "")
        self.assertEqual(noErrorCommand, "")

        self.assertEqual(noErrorUpper, "")
        self.assertEqual(lowerErrorU, "CMake commands should be uppercase")
        self.assertEqual(mixedErrorU, "CMake commands should be uppercase")

    def test_checkCommandUpperLowerCaseLOWER(self):
        """Check if the commands are in LOWER case."""
        # Given
        optionsLower = {
            "commandsStyle": "lowercase"
        }

        upperCommand = "FIND_PACKAGE()"
        lowerCommand = "find_package()"
        mixedCommand = "FiNd_PaCkAgE()"

        # When
        upperErrorL = linecheckers.checkCommandUpperLowerCase(upperCommand,
                                                              optionsLower)
        noErrorLower = linecheckers.checkCommandUpperLowerCase(lowerCommand,
                                                               optionsLower)
        mixedError = linecheckers.checkCommandUpperLowerCase(mixedCommand,
                                                             optionsLower)\

        # Then
        self.assertEqual(upperErrorL, "CMake commands should be lowercase")
        self.assertEqual(noErrorLower, "")
        self.assertEqual(mixedError, "CMake commands should be lowercase")

    def test_checkCommandUpperLowerCaseMIXED(self):
        """Check if the commands are in mixed case."""
        # Given
        optionsMixed = {
            "commandsStyle": "mixed"
        }

        upperCommand = "FIND_PACKAGE()"
        lowerCommand = "find_package()"
        mixedCommand = "FiNd_PaCkAgE()"

        # When
        upperNE = linecheckers.checkCommandUpperLowerCase(upperCommand,
                                                          optionsMixed)
        lowerNE = linecheckers.checkCommandUpperLowerCase(lowerCommand,
                                                          optionsMixed)
        mixedNE = linecheckers.checkCommandUpperLowerCase(mixedCommand,
                                                          optionsMixed)

        # Then
        self.assertEqual(upperNE, "")
        self.assertEqual(lowerNE, "")
        self.assertEqual(mixedNE, "")


if __name__ == '__main__':
    unittest.main()
