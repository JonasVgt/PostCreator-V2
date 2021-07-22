
from package.parser.document_parser import DocumentParser
from package.parser.simple_insert_parser import SimpleInsertParser

class ParagraphParser(SimpleInsertParser):
    _identifier :str = "p"
    _html_insert :str = "</p>\n<p>"

DocumentParser.parsers.append(ParagraphParser)