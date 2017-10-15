"""One line checkers.

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
import yacl.parser as parser


def checkLineLength(line, options):
    """Check for lines longer than the recommended length."""
    try:
        if "S001" in options["rules"]["oneLineIgnores"]:
            return ""
    except KeyError:
        pass
    if len(line) > options["lineLength"]:
        return "Length of the line is more than " + \
                str(options["lineLength"]) + \
                " (" + str(len(line)) + ")"
    return ""


def checkCommandUpperLowerCase(line, options):
    """Check if the commands are upper or lower case."""
    try:
        if "S002" in options["rules"]["oneLineIgnores"]:
            return ""
    except KeyError:
        pass

    command = parser.getCMakeCommand(line)
    if command:
        if options["commandsStyle"] == "uppercase":
            upper = command.upper()
            if upper != command:
                message = "uppercase"
            else:
                return ""
        elif options["commandsStyle"] == "lowercase":
            lower = command.lower()
            if lower != command:
                message = "lowercase"
            else:
                return ""
        elif options["commandsStyle"] == "mixed":
            return ""
        return "CMake commands should be " + message
    return ""
