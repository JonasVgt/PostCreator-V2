from package.parser.document_parser import DocumentParser
from package.parser.simple_enclosing_parser import SimpleEnclosingParser

class SubsectionParser(SimpleEnclosingParser):
    _identifier :str = "subsection"
    _html_start :str = "<h3>"
    _html_end :str = "</h3>"

DocumentParser.parsers.append(SubsectionParser)