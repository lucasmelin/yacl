"""Parser functions.

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
import re


def getCMakeCommand(line):
    """Search for a cmake command in the given line."""
    regex = re.compile(r'^\s*(\w+)(\s*)\(', re.VERBOSE)
    match = regex.match(line)
    if match:
        return match.group(1)
    return None