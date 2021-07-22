
from package.parser.simple_insert_parser import SimpleInsertParser
from package.parser.base_parser import BaseParser

class CurlyCloseParser(SimpleInsertParser):
    _identifier :str = "curly_right"
    _html_insert :str = "&#x7D;"

BaseParser.parsers.append(CurlyCloseParser)