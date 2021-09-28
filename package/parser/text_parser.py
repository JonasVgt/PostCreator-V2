
from package.parser.parser import Parser


class TextParser(Parser):

    def __init__(self, input:str, start :int = 0, end:int = -1) -> None:
        self._input = input
        self._start = start
        if(end < 0):
            self._end = len(input)
        else:
            self._end = end


  
    def parse(self) -> str:
        return self._input[self._start:self._end]

