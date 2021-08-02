
from package.post_encoder import PostEncoder
from package.project import Project
from typing import Any
from package.post import Post
import json

class ProjectEncoder(json.JSONEncoder):
    
    def default(self, obj: Any) -> Any:
        if not isinstance(obj,Project):
            return super(ProjectEncoder,self).default(obj)
            
        posts = []
        for post in obj.posts:
            posts.append(PostEncoder().default(post))


        return {
            'id': obj.id,
            'title':obj.title,
            'public':obj.public,
            'posts':posts
        }
        