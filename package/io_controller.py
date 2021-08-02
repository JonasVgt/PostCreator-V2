import os
from package.project_decoder import ProjectDecoder
from package.post import Post
from package.project import Project
import json

class IOController:

    @staticmethod
    def load_project(path:str) -> Project:
        if(not os.path.exists("./project.cfg") or not os.path.isfile("./project.cfg")):
            raise IOError("could not find a project.cfg")

        file = open(os.path.join(path,'project.cfg'))
        return json.load(file, cls=ProjectDecoder)

    @staticmethod
    def load_post(path:str) -> str:
        if(not os.path.exists(path) or not os.path.isfile(path)):
            raise IOError(f"could not find the post file at {path}")
        file = open(path)
        return file.read()


    @staticmethod
    def create_project(path, Project):
        pass


    @staticmethod
    def find_unique_name(path:str, title:str, extension:str) -> str:
        name = title.title().replace(' ','')
        for i in range(1000):
            if(i == 0):
                filename = f'{name}{extension}'
            else:
                filename = f'{name} ({i}){extension}'

            path = os.path.join(path,filename)

            if(os.path.exists(path)):
                continue
            
            return path
        raise IOError("Could not generate new unique filename within 1000 tries")
        