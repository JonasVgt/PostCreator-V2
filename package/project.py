import json
import os
import shutil
from datetime import date
import re
from typing import Dict, List, Union

class Project:

    @staticmethod
    def create(title:str,project_id:int):
        path = os.path.join("./projects/", Project.getUniqueName("./projects",title=title))

        shutil.copytree(src="./default_project", dst=path)

        project = Project(path=path)
        project.set_id(project_id)
        project.set_title(title)
        project.write()
        return project

    def __init__(self, path: str) -> None:
        self.path = path
        self.load()

    def load(self) -> None:
        file = open(os.path.join(self.path,"project.cfg"), 'r')
        self.config = json.load(file)

    def write(self) -> None:
        file = open(os.path.join(self.path,"project.cfg"), 'w')
        file.write(json.dumps(obj=self.config,indent=4))

    def get_id(self) -> int:
        return self.config['id']

    def set_id(self, id: int) -> None:
        self.config['id'] = id

    def get_title(self) -> str:
        return self.config['title']

    def set_title(self, title:str) -> None:
        self.config['title'] = title

    def get_posts(self) -> List[Dict[str,str]]:
        return self.config['posts']
    
    def get_post(self,id:int) -> Union[None,Dict[str,str]]:
        for post in self.get_posts():
            if(post['id'] == id):
                return post
        return None


    def add_post(self,post_id:int,title:str) -> Dict[str,str]:
        path = os.path.join("./",Project.getUniqueName("./",title=title)+".post")

        open(path, 'a').close()

        post = {
            'id':post_id,
            'title': title,
            'date':  date.today().isoformat(),
            'path': path
        }
        self.config['posts'].append(post)
        return post

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