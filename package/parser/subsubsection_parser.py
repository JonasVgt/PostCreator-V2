from package.parser.document_parser import DocumentParser
from package.parser.simple_enclosing_parser import SimpleEnclosingParser

class SubsubsectionParser(SimpleEnclosingParser):
    _identifier :str = "subsection"
    _html_start :str = "<h4>"
    _html_end :str = "</h4>"

DocumentParser.parsers.append(SubsubsectionParser)