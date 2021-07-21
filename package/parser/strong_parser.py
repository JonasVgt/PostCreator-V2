from io import StringIO
from package.parser.simple_enclosing_parser import SimpleEnclosingParser
from package.parser.base_parser import BaseParser

class StrongParser(SimpleEnclosingParser):
    _identifier :str = "st"
    _html_start :str = "<strong>"
    _html_end :str = "</strong>"


BaseParser.parsers.append(StrongParser)