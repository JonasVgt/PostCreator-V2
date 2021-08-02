from dataclasses import dataclass
from package.post import Post
from typing import Any, Dict, List, Optional


@dataclass
class Project:

    path:str
    id:int
    title:str
    public:bool
    posts:List[Post]

        


    def find_post(self,id:int) -> Optional[Post]:
        """returns post with specific id"""
        for post in self.posts:
            if(post.id == id):
                return post
        return None

    def add_post(self,post:Post) -> None:
        """adds post to the project"""
        self.posts.append(post)

