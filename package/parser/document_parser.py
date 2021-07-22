from package.parser.base_parser import BaseParser
from package.errors import ParseError

class DocumentParser(BaseParser):


    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = start
        self._fields = []
        self.tokenize()



    def processToken(self,pos:int) -> int:
        for parser in self.parsers:
            if(parser.matches(self._input,pos)):
                p = parser(self._input,pos)
                self._fields.append(p)
                return p.end()
        
        raise ParseError(f'No valid parser found for: {self._input[pos:pos+20]} [...]')


    def before(self) -> str:
        return '<p>'

    def after(self) -> str:
        return '</p>'

    def findEnd(self, start:int, end:int) -> int:
        
        if(end < len(self._input)):
            return -1
        else:
            return len(self._input)


