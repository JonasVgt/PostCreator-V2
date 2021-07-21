
from package.parser.simple_enclosing_parser import SimpleEnclosingParser
from package.parser.base_parser import BaseParser

class EmParser(SimpleEnclosingParser):
    _identifier :str = "em"
    _html_start :str = "<em>"
    _html_end :str = "</em>"

BaseParser.parsers.append(EmParser)