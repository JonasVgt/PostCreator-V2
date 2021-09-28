from dataclasses import dataclass
import os
from package.parser.preprocessor import Preprocessor
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
        if(not os.path.exists(self.path)):
            open(self.path, 'x')
        input = open(self.path, 'r').read()
        preprocessed = Preprocessor.process(input)
        parser = DocumentParser(preprocessed,0)
        return parser.parse()


    @staticmethod
    def load(obj : Dict[str,Any]) -> 'Post':
        try:
            if(type(obj['public']) != bool):
                raise ValueError(f'parameter public must be of type bool but is '+ str(type(obj['public'])))
            post = Post(
            id=int(obj['id']),
            title=str(obj['title']),
            date=datetime.date.fromisoformat(obj['date']),
            path=str(obj['path']),
            public=obj['public']            
            )
            return post
        except KeyError as e:
            raise ValueError(f"Missing Parameter: '{e.args[0]}'")
    
    @staticmethod
    def dump(obj: 'Post') -> Dict[str,Any]:
        return{
            'id':obj.id,
            'title': obj.title,
            'date':  obj.date.isoformat(),
            'path': obj.path,
            'public':obj.public
        }




