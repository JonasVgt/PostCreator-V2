from package.parser.document_parser import DocumentParser
from package.parser.simple_enclosing_parser import SimpleEnclosingParser

class SubsubsectionParser(SimpleEnclosingParser):
    _identifier :str = "subsection"
    _html_start :str = "</p><h4>"
    _html_end :str = "</h4><p>"

DocumentParser.parsers.append(SubsubsectionParser)