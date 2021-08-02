from typing import Any
from package.post import Post
import json
import datetime


class PostDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.hook, *args, **kwargs)


    def hook(self, obj):        
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
    