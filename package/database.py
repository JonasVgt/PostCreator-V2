import json
from typing import Dict
from package.config import Config
import mysql.connector


class Database:

    database = None

    @classmethod
    def getDatabase(cls):
        if(cls.database):
            return cls.database

        config = Config()
        db = Database(
            host=config.get(f"db_host"),
            user=config.get(f"db_user"),
            password=config.get(f"db_password"),
            db_name=config.get(f"db_database")
            )
        cls.database = db
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


    def create_post(self,post_id:int,project_id:int, title:str,text:str, date:str, public:bool) -> int:
        sql = "INSERT INTO posts (project_id,post_id, title,date,text, public) VALUES (%s, %s, %s, %s, %s, %s);"
        values = (project_id,post_id, title, date,text, public)
        self.cursor.execute(sql,values)
        self.connection.commit()
        return post_id

    def create_project(self,project_id:int,title:str,public:bool) -> int:
        sql = "INSERT INTO projects (project_id, title, public) VALUES (%s, %s, %s);"
        values = (project_id,title, public)
        self.cursor.execute(sql,values)
        self.connection.commit()
        return project_id


    def update_project(self,project_id:int, title:str,public:bool) -> None:
        sql = "UPDATE projects SET title = %s, public = %s WHERE project_id = %s;"
        values = (title,public,project_id)
        self.cursor.execute(sql,values)
        self.connection.commit()



    def update_post(self,project_id:int, post_id:int, title:str, date:str, text:str, public:bool) -> None:
        sql = "UPDATE posts SET title = %s, date = %s, text=%s, public=%s WHERE project_id = %s AND post_id = %s;"
        values = (title,date,  text,public,project_id,post_id)
        self.cursor.execute(sql,values)
        self.connection.commit()
        
    def get_largest_project_id(self) -> int:
        sql = "SELECT project_id FROM projects ORDER BY project_id DESC LIMIT 1;"
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        if(not res):
            return 0
        
        (id,) = res # type: ignore
        return id

    def get_largest_post_id(self,project_id:int) -> int:
        sql = "SELECT post_id FROM posts WHERE project_id = %s ORDER BY post_id DESC LIMIT 1;"
        values = (project_id,)
        self.cursor.execute(sql,values)
        res = self.cursor.fetchone()
        if(not res):
            return 0
        (id,) = res # type: ignore
        return id


