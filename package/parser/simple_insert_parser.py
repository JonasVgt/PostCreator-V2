from package.parser.parser import Parser
import re
from package.errors import ParseError

class SimpleInsertParser(Parser):

    _identifier :str = "simple"
    _html_insert :str = "<simple>"

    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = self.processIdentifier()
        self._append_space = False
        

    def processIdentifier(self) -> int:
        
        pattern = re.compile(rf'\\{{{self._identifier}}}')
        match = pattern.match(self._input,self._start)

        if (not match):
            pattern = re.compile(rf'\\{self._identifier}')
            match = pattern.match(self._input,self._start)
            self._append_space = True
            if(not match):
                raise ParseError(f'Identifier of {type(self)} does not match: {self._input[self._start:self._start+20]} [...]')
        
        return match.end()

  
    def parse(self) -> str:
        """
        Parses this and all the contained fields

        @returns: the parsed text  

        """
        out = self._html_insert
        if(self._append_space):
            out += " " 
        return out


    @classmethod
    def matches(cls, input:str, pos:int) -> bool:
        """
        @params:
        input: the input string
        pos: the position, where this Parser should be tested

        @returns: True, if the identifier matches
        """

        pattern = re.compile(rf'\\{cls._identifier} |\\{{{cls._identifier}}}')
        return bool(pattern.match(input,pos))
