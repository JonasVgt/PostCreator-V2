from io import StringIO
from package.parser.text_parser import TextParser
from package.parser.parser import Parser
import re
from typing import List, Type
from package.errors import ParseError

class BaseParser(Parser):

    parsers : List[Type[Parser]] = []

    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = start
        self._fields : List[Parser] = []
        self.tokenize()


    def tokenize(self):
        """
        tokenizes all the whole input and sets the end() to the position of the charater directly after the last character of this field

        
        """
        pos = self.processIdentifier()
        while(True):
            next_token = self.findNextToken(pos)
            
            if(next_token == -1):
                closingToken = self.findEnd(pos,len(self._input))
                if(closingToken != -1):
                    self.processText(pos,closingToken)
                    return
                else:
                    raise ParseError(f'Not end found for the field of type {type(self)} starting at {self.start()}')
                    
            closingToken = self.findEnd(pos,next_token)
            if(closingToken != -1):
                self.processText(pos,closingToken)
                return
            
            self.processText(pos,next_token)
            pos = self.processField(next_token)

    def processField(self,pos:int) -> int:
        """
        processes a field 

        @param: 
        pos: position of the first character of the token to be processed  

        @returns: the position of character directly after the end of the processed field
        
        """
        for parser in self.parsers:
            if(parser.matches(self._input,pos)):
                p = parser(self._input,pos)
                self._fields.append(p)
                return p.end()
        
        raise ParseError(f'No valid parser found for: {self._input[pos:pos+20]} [...]')

    def processText(self,start:int,end:int):
        if(start!=end):
            self._fields.append(TextParser(self._input,start,end))

    def processIdentifier(self) -> int:
        """
        Processes own Identifier at the beginning of the input

        @returns: the position of the character directly after the end of own Identifier

        """
        return self._start


    def findNextToken(self, start :int) -> int:
        """
        finds the next Token.

        @param:
        start: the position of the first character from where the search is started

        @returns: the position of the first character a found token. If no token is found -1 is returned
        """
        pattern = re.compile(r'\\')
        res = pattern.search(self._input, start)
        pos = -1
        if(res):
            pos = res.start()
        return pos
        

    def findEnd(self, start:int, end:int) -> int:
        """
        tests if this field is ending between start and end. If it ends, self._end will be set to the position of the character directly after the last one of this field

        @params:
        start: the position of the first character from where the search is started
        end: the last searched chacter is the one of index end-1

        @returns: If this field should not end, -1 is returned, else the position after the last character which should be processed in this field

        """
        pattern = re.compile(r'}')
        res = pattern.search(self._input,start,end)
        pos = -1
        if(res):
            self._end = res.end()
            pos = res.start()
        return pos

    
    def before(self) -> str:
        """
        @returns: a string, which will be added to the beginning the parsed field
        """
        return ""

    def after(self) -> str:
        """
        @returns: a string, which will be appended to the end of the parsed field
        """
        return ""

    def parse(self) -> str:
        """
        Parses this and all the contained fields

        @returns: the parsed text  

        """
        output = StringIO()
        output.write(self.before())
        for field in self._fields:
            output.write(field.parse())
        output.write(self.after())
        return output.getvalue()
