
class Parser:

    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = start


    def start(self) -> int:
        """
        returns the position of the first character of this field

        @returns: start position
        """
        return self._start
    
    def end(self) -> int:
        """
        returns the position of the character directly after the last one from this field

        @returns: end position
        """
        return self._end

  
    def parse(self) -> str:
        """
        Parses this and all the contained fields

        @returns: the parsed text  

        """

        return ""

