from typing import List
from package.parser.base_parser import BaseParser
from package.parser.parser import Parser
import re
from package.errors import ParseError

class SimpleEnclosingParser(BaseParser):

    _identifier :str = "simple"
    _html_start :str = "<simple>"
    _html_end :str = "</simple>"

    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = start
        self._fields : List[Parser] = []
        self.tokenize()


    def before(self) -> str:
        return self._html_start

    def after(self) -> str:
        return self._html_end   
