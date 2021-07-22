
from package.parser.simple_insert_parser import SimpleInsertParser
from package.parser.base_parser import BaseParser

class BackslashParser(SimpleInsertParser):
    _identifier :str = r"\\"
    _html_insert :str = "&#x5C;"

BaseParser.parsers.append(BackslashParser)