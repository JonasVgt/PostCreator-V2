from dataclasses import dataclass
import json
import os
from package.post import Post
import shutil
from datetime import date
from typing import List, Optional


@dataclass
class Project:

    id : int
    title : str
    public : bool
    path : str
    posts: List[Post]

    @staticmethod
    def create(title:str,project_id:int) -> 'Project':
        path = os.path.join("./projects/", Project.getUniqueName("./projects",title=title))

        shutil.copytree(src="./default_project", dst=path)

        project = Project(path=path,id=project_id,public=False,title=title, posts=[])
        project.write()
        return project

    @staticmethod
    def load(path:str) -> 'Project':
        file = open(os.path.join(path,"project.cfg"), 'r')
        config = json.load(file)
        try:
            posts = []
            if(type(config['posts']) != list):
                raise ValueError(f'parameter public must be of type list but is '+ str(type(config['posts'])))


            for post_dict in config['posts']:
                posts.append(Post.load(post_dict))

            if(type(config['public']) != bool):
                raise ValueError(f'parameter public must be of type bool but is '+ str(type(config['public'])))

            return Project(
                path=path,
                id = int(config['id']),
                title=str(config['title']),
                public=bool(config['public']),
                posts=posts
            )

        except KeyError as e:
            raise ValueError(f"Missing Parameter: '{e.args[0]}'")

    def write(self) -> None:
        posts = []
        for post in self.posts:
            posts.append(Post.dump(post))


        config = {
            'id': self.id,
            'title':self.title,
            'public':self.public,
            'posts':posts
        }

        file = open(os.path.join(self.path,"project.cfg"), 'w')
        file.write(json.dumps(obj=config,indent=4))


    
    def get_post(self,id:int) -> Optional[Post]:
        for post in self.posts:
            if(post.id == id):
                return post
        return None


    def add_post(self,post:Post):
        self.posts.append(post)


    @staticmethod
    def getUniqueName(root:str,title:str) -> str:
        for i in range (1000):
            filename = title.title().replace(" ","")
            if(i != 0):
                  filename += f'({i})'
            path = os.path.join(root,filename)
            if(not os.path.exists(path)):
                return filename
        raise FileExistsError("Could not get uniqe name after 1000 tries")