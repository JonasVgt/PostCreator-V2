from io import StringIO
from package.parser.base_parser import BaseParser
from package.parser.text_parser import TextParser
from package.parser.parser import Parser
import re
from typing import List, Type
from package.errors import ParseError

class EnumParser(BaseParser):


    def __init__(self, input:str, start:int) -> None:
        self._input = input
        self._start = start
        self._end = start
        self._items: List[List[Parser]] = []
        self._fields: List[Parser] = []
        self._item_read : bool = False
        self.tokenize()
        self._items.append(self._fields)




    def processField(self,pos:int) -> int:
        """
        processes a field 

        @param: 
        pos: position of the first character of the token to be processed  

        @returns: the position of character directly after the end of the processed field
        
        """
        if(self.matches_item(self._input,pos)):
            return self.processItem(pos)

        return super().processField(pos)



    def processIdentifier(self) -> int:
        """
        Processes own Identifier at the beginning of the input

        @returns: the position of the character directly after the end of own Identifier

        """
        pattern = re.compile(r'\\enum{ *')
        match = pattern.match(self._input,self._start)
        if(not match):
            raise ParseError(f'Identifier of {type(self)} does not match: {self._input[self._start:self._start+20]} [...]')
        
        return match.end()

    def processItem(self, pos:int):
        pattern = re.compile(rf'\\{{item}}')
        match = pattern.match(self._input,pos)

        if (not match):
            pattern = re.compile(rf'\\item ')
            match = pattern.match(self._input,pos)
            self._append_space = True
            if(not match):
                raise ParseError(f'Identifier of Item does not match: {self._input[pos:pos+20]} [...]')
        
        if(not self._item_read):
            if(len(self._fields) != 0):
                raise ParseError(f"Item tag missing at: {self._input[self._start:self._start+20]}")
                
            self._item_read = True
        else:
            self._items.append(self._fields)
            self._fields = []
        return match.end()


    
    def before(self) -> str:
        """
        @returns: a string, which will be added to the beginning the parsed field
        """
        return "<ol>"

    def after(self) -> str:
        """
        @returns: a string, which will be appended to the end of the parsed field
        """
        return "</ol>"

    def parse(self) -> str:
        """
        Parses this and all the contained fields

        @returns: the parsed text  

        """
        output = StringIO()
        output.write(self.before())
        for item in self._items:
            output.write('<li>')
            for field in item:
                output.write(field.parse())
            output.write('</li>')
        output.write(self.after())
        return output.getvalue()

    @classmethod
    def matches_item(cls, input:str, pos:int) -> bool:
        """
        @params:
        input: the input string
        pos: the position, where this Parser should be tested

        @returns: True, if the identifier matches
        """

        pattern = re.compile(rf'\\item |\\{{item}}')
        return bool(pattern.match(input,pos))


    @classmethod
    def matches(cls, input:str, pos:int) -> bool:
        """
        @params:
        input: the input string
        pos: the position, where this Parser should be tested

        @returns: True, if the identifier matches
        """
        pattern = re.compile(r'\\enum{')
        return bool(pattern.match(input,pos))

BaseParser.parsers.append(EnumParser)