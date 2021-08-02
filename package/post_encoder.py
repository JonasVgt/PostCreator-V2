from typing import Any
from package.post import Post
import json

class PostEncoder(json.JSONEncoder):
    
    def default(self, obj: Any) -> Any:
        if not isinstance(obj,Post):
            return super(PostEncoder,self).default(obj)
        
        return{
            'id':obj.id,
            'title': obj.title,
            'date':  obj.date.isoformat(),
            'path': obj.path,
            'public':obj.public
        }
            
