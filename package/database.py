import json
from typing import Dict
from package.config import Config
import mysql.connector


class Database:

    databases :Dict[str,'Database'] = {}

    @classmethod
    def getDevDatabase(cls):
        return cls.getDatabase("dev")

    
    @classmethod
    def getPubDatabase(cls):
        return cls.getDatabase("pub")

    @classmethod
    def getDatabase(cls, name:str):
        db = cls.databases[name]
        if(db):
            return db

        config = Config()
        db = Database(
            host=config.get(f"db_{name}_host"),
            user=config.get(f"db_{name}_user"),
            password=config.get(f"db_{name}_password"),
            db_name=config.get(f"db_{name}_database")
            )
        cls.databases[name] = db
        return db

    def __init__(self, host:str,user:str,password:str,db_name:str) -> None:

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.cursor : mysql.connector.connection.CursorBase = self.connection.cursor()

    def __del__(self):
        self.connection.close()


    def create_post(self,post_id,project_id, title,text, date) -> int:
        sql = "INSERT INTO posts (project_id,post_id, title,date,text) VALUES (%s, %s, %s, %s, %s);"
        values = (project_id,post_id, title, date,text)
        self.cursor.execute(sql,values)
        self.connection.commit()
        return post_id

    def create_project(self,project_id,title) -> int:
        sql = "INSERT INTO projects (project_id, title) VALUES (%s, %s);"
        values = (project_id,title)
        self.cursor.execute(sql,values)
        self.connection.commit()
        return project_id


    def update_project(self,project_id, title):
        sql = "UPDATE projects SET title = %s WHERE project_id = %s"
        values = (title,project_id)
        self.cursor.execute(sql,values)
        self.connection.commit()


    def update_post(self,project_id, post_id, title, date, text):
        sql = "UPDATE posts SET title = %s, date = %s, text=%s WHERE project_id = %s AND post_id = %s "
        values = (title,date, text,project_id,post_id)
        self.cursor.execute(sql,values)
        self.connection.commit()
        
    def get_largest_project_id(self) -> int:
        sql = "SELECT project_id FROM projects ORDER BY project_id DESC LIMIT 1;"
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        if(not res):
            return 1
        
        (id,) = res # type: ignore
        return id
    
    def project_exists(self,project_id):
        sql = "SELECT TOP 1 project_id FROM projects WHERE project_id = %s"
        values = (project_id,)
        self.cursor.execute(sql,values)
        return bool(self.cursor.fetchone())

    def post_exists(self,project_id,post_id):
        sql = "SELECT TOP 1 post_id FROM posts WHERE project_id = %s AND post_id = %s"
        values = (project_id,post_id)
        self.cursor.execute(sql,values)
        return bool(self.cursor.fetchone())

    def get_largest_post_id(self,project_id:int) -> int:
        sql = "SELECT post_id FROM posts WHERE project_id = %s ORDER BY post_id DESC LIMIT 1;"
        values = (project_id,)
        self.cursor.execute(sql,values)
        res = self.cursor.fetchone()
        if(not res):
            return 1
        (id,) = res # type: ignore
        return id


