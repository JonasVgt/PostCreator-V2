from package.parser.document_parser import DocumentParser
from package.parser.simple_enclosing_parser import SimpleEnclosingParser

class SectionParser(SimpleEnclosingParser):
    _identifier :str = "section"
    _html_start :str = "</p><h2>"
    _html_end :str = "</h2><p>"

DocumentParser.parsers.append(SectionParser)