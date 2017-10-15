"""Lint a cmake file or directory.

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
from __future__ import absolute_import
from inspect import getmembers
from inspect import isfunction
import yacl.linecheckers as linecheckers


class YACL(object):
    """Class of the linter."""

    def __init__(self, configuration):
        """Init the linter.

        :param configuration: override lintern configuration.
        :type configuration: dict.
        """
        self.totalErrors = 0
        self.lineOptions = {
            "lineLength": 80,
            "commandsStyle": "uppercase"
        }

    def lintFile(self, fileName):
        """Lint one cmake file.

        :param fileName: path to the file to lint.
        :type fileName: str.
        """
        with open(fileName) as fileToLint:
            cmakeFile = fileToLint.read()
            lines = cmakeFile.split("\n")
            lineNumber = 0
            for l in lines:
                message = self.__lintLine(l)
                # pylint: disable=C0325
                print(fileName + ":" + str(lineNumber) + " " + message)
                lineNumber += 0

    def __lintLine(self, line):
        """Run the checkers for the line passed as an argument.

        :param line: line to lint.
        :type line: str.
        :return: error message.
        :rtype: str.
        """
        checkers = getmembers(linecheckers, isfunction)
        for c in checkers:
            message = c[1](line, self.lineOptions)
            return message
