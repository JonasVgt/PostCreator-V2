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


    def processIdentifier(self) -> int:
        """
        Processes own Identifier at the beginning of the input

        @returns: the position of the character directly after the end of own Identifier

        """
        pattern = re.compile(rf'\\{self._identifier}{{')
        match = pattern.match(self._input,self._start)
        if(not match):
            raise ParseError(f'Identifier of {type(self)} does not match: {self._input[self._start:self._start+20]} [...]')
        
        return match.end()

    def before(self) -> str:
        """
        @returns: a string, which will be added to the beginning the parsed field
        """
        return self._html_start

    def after(self) -> str:
        """
        @returns: a string, which will be appended to the end of the parsed field
        """
        return self._html_end   


    @classmethod
    def matches(cls, input:str, pos:int) -> bool:
        """
        @params:
        input: the input string
        pos: the position, where this Parser should be tested

        @returns: True, if the identifier matches
        """
        pattern = re.compile(rf'\\{cls._identifier}{{')
        return bool(pattern.match(input,pos))
