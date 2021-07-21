#!/usr/bin/env python3

import os
from package.parser import DocumentParser
from package.project import Project
import sys
from package.database import Database


def create_post(db:Database,args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator post create <title>")

    if(not os.path.exists("./project.cfg") or not os.path.isfile("./project.cfg")):
        sys.exit("This function must be called from inside a project folder")

    title = args[3]
    project = Project("./")
    post_id = db.get_largest_post_id(project_id=project.get_id())+1
    post = project.add_post(post_id,title)
    project.write()
    post_id = db.create_post(post_id=post_id, project_id=project.get_id(),title=title,text="",date=post['date'])



def create_project(db:Database,args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator project create <title>")

    title = args[3]
    project_id = db.get_largest_project_id()+1
    Project.create(title=title,project_id=project_id)
    db.create_project(project_id=project_id,title=title)
    

def push_project(db:Database,args):
    if(len(args) != 3):
        sys.exit("Usage: postcreator project push")

    project = Project("./")
    db.update_project(project_id=project.get_id(),title=project.get_title())

    for post in project.get_posts():
        push_post_id(db=db,id=post['id'])


def pull_project(db:Database,args):#TODO Implement
    pass

def push_post(db:Database,args):
    if(len(args) != 4):
        sys.exit("Usage: postcreator post push <id>")

    id :int = int(args[3])
    push_post_id(db,id)



def push_post_id(db:Database,id:int):
    project = Project("./")
    post = project.get_post(id)
    if(not post):
        sys.exit("No post with that ID")
    file = open(post['path'],'r')
    parser = DocumentParser(file.read(),0)
    db.update_post(project_id=project.get_id(),post_id=id,title=post['title'],date=post['date'],text=parser.parse())
    pass

def pull_post(db:Database,args):#TODO Implement
    pass


def remove_post(db:Database,args):#TODO Implement
    pass


def remove_project(db:Database,args):#TODO Implement
    pass



def start_watchdog(db:Database,args):#TODO Implement
    pass





if __name__ == '__main__':
    if(len(sys.argv) < 3):
        sys.exit("Usage: postcreator <post | project | watchdog> <command> [args]") 


    database =  Database()

    if(sys.argv[1].__eq__("post")):
        if(sys.argv[2].__eq__("create")):
            create_post(database,sys.argv)
        elif(sys.argv[2].__eq__("remove")):
            remove_post(database,sys.argv)
        elif(sys.argv[2].__eq__("push")):
            push_post(database,sys.argv)
        elif(sys.argv[2].__eq__("pull")):
            pull_post(database,sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'create', 'remove', 'push', 'pull'")

        pass
    elif(sys.argv[1].__eq__("project")):
        if(sys.argv[2].__eq__("create")):
            create_project(database,sys.argv)
        elif(sys.argv[2].__eq__("remove")):
            remove_project(database,sys.argv)
        elif(sys.argv[2].__eq__("push")):
            push_project(database,sys.argv)
        elif(sys.argv[2].__eq__("pull")):
            pull_project(database,sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'create', 'remove', 'push', 'pull'")
    elif(sys.argv[1].__eq__("watchdog")):
        if(sys.argv[2].__eq__("start")):
            start_watchdog(database,sys.argv)
        else:
            sys.exit("Second Argument must be one of: 'start'")
    else:
        sys.exit("First Argument must be one of: 'post', 'project', 'watchdog'")


