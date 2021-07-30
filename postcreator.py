#!/usr/bin/env python3

import os
from package.parser.preprocessor import Preprocessor
from package.parser import DocumentParser
from package.project import Project
import sys
from package.database import Database


def create_post(args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator post create <title>")

    if(not os.path.exists("./project.cfg") or not os.path.isfile("./project.cfg")):
        sys.exit("This function must be called from inside a project folder")

    db = Database.getDatabase()

    title = args[3]
    project = Project("./")
    post_id = db.get_largest_post_id(project_id=project.get_id())+1
    post = project.add_post(post_id,title)
    project.write()
    post_id = db.create_post(post_id=post_id, project_id=project.get_id(),title=title,text="",date=post['date'],public=bool(post['public']))



def create_project(args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator project create <title>")

    db = Database.getDatabase()

    title = args[3]
    project_id = db.get_largest_project_id()+1
    Project.create(title=title,project_id=project_id)
    db.create_project(project_id=project_id,title=title, public=False)
    

def push_project(args):
    if(len(args) != 3):
        sys.exit("Usage: postcreator project push")

    db = Database.getDatabase()

    project = Project("./")
    db.update_project(project_id=project.get_id(),title=project.get_title(),public=project.get_public())

    for post in project.get_posts():
        push_post_id(id=int(post['id']))


def pull_project(args):#TODO Implement
    pass

def push_post(args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator post push <id>")

    id :int = int(args[3])
    push_post_id(id)



def push_post_id(id:int):
    project = Project("./")
    post = project.get_post(id)
    if(not post):
        sys.exit("No post with that ID")
    input = open(post['path'],'r').read()
    preprocessed = Preprocessor.process(input)
    parser = DocumentParser(preprocessed,0)
    db = Database.getDatabase()

    db.update_post(project_id=project.get_id(),post_id=id,title=post['title'],date=post['date'],text=parser.parse(),public=bool(post['public']))
    


def pull_post(args):#TODO Implement
    pass


def remove_post(args):#TODO Implement
    pass


def remove_project(args):#TODO Implement
    pass



def start_watchdog(args):#TODO Implement
    pass





if __name__ == '__main__':
    if(len(sys.argv) < 3):
        sys.exit("Usage: postcreator <post | project | watchdog> <command> [args]") 

    if(sys.argv[1].__eq__("post")):
        if(sys.argv[2].__eq__("create")):
            create_post(sys.argv)
        elif(sys.argv[2].__eq__("remove")):
            remove_post(sys.argv)
        elif(sys.argv[2].__eq__("push")):
            push_post(sys.argv)
        elif(sys.argv[2].__eq__("pull")):
            pull_post(sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'create', 'remove', 'push', 'pull'")

        pass
    elif(sys.argv[1].__eq__("project")):
        if(sys.argv[2].__eq__("create")):
            create_project(sys.argv)
        elif(sys.argv[2].__eq__("remove")):
            remove_project(sys.argv)
        elif(sys.argv[2].__eq__("push")):
            push_project(sys.argv)
        elif(sys.argv[2].__eq__("pull")):
            pull_project(sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'create', 'remove', 'push', 'pull'")
    elif(sys.argv[1].__eq__("watchdog")):
        if(sys.argv[2].__eq__("start")):
            start_watchdog(sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'start'")
    else:
        sys.exit("First Argument must be one of: 'post', 'project', 'watchdog'")


