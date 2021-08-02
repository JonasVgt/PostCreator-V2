from package.project import Project
from package.post_decoder import PostDecoder
from typing import Any
from package.post import Post
import json
import datetime


class ProjectDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.hook, *args, **kwargs)


    def hook(self, obj):        

        try:
            posts = []
            if(type(obj['posts']) != list):
                raise ValueError(f'parameter public must be of type list but is '+ str(type(obj['posts'])))


            for post_dict in obj['posts']:
                posts.append(PostDecoder().hook(post_dict))

            if(type(obj['public']) != bool):
                raise ValueError(f'parameter public must be of type bool but is '+ str(type(obj['public'])))

            return Project(
                path="path",#TODO implement
                id=int(obj['id']),
                title=str(obj['title']),
                public=bool(obj['public']),
                posts=obj
            )
        except KeyError as e:
            raise ValueError(f"Missing Parameter: '{e.args[0]}'")
    