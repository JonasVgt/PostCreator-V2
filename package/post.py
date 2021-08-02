from dataclasses import dataclass
from package.post_encoder import PostEncoder
from package.io_controller import IOController
from package.parser.document_parser import DocumentParser
from typing import Any, Dict
import datetime



@dataclass
class Post:
    id : int 
    title : str
    path : str
    public : bool
    date : datetime.date = datetime.date.today()

    

    def parse(self) -> str:
        input = IOController.load_post(self.path)
        parser = DocumentParser(input,0)
        return parser.parse()


