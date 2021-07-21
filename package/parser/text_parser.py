
from package.parser.parser import Parser


class TextParser(Parser):

    def __init__(self, input:str, start:int, end:int) -> None:
        self._input = input
        self._start = start
        self._end = end


  
    def parse(self) -> str:
        """
        Parses this and all the contained fields

        @returns: the parsed text  

        """

        return self._input[self._start:self._end]

