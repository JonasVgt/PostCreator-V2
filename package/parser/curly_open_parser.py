
from package.parser.simple_insert_parser import SimpleInsertParser
from package.parser.base_parser import BaseParser

class CurlyOpenParser(SimpleInsertParser):
    _identifier :str = "curly_left"
    _html_insert :str = "&#x7B;"

BaseParser.parsers.append(CurlyOpenParser)