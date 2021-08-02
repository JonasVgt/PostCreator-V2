import datetime
from typing import Type
import package.project as pr
import package.post as p
import unittest

class TestProject(unittest.TestCase):
    

    def test_load_project(self):
        self.assertEqual(
            pr.Project.load_project({
                'id':0,
                'title':'title',
                'public':False,
                'posts':[]
            },'/project/'),
            pr.Project(path="/project/",id=0,title="title",public=False,posts=[])
        )
        self.assertEqual(
            pr.Project.load_project({
                'id':-5001,
                'title':'',
                'public':True,
                'posts': [
                    {
                    "id":"0",
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post"
                    }]
            },'abc'),
            pr.Project(path="abc",id=-5001,title='',public=True,posts=[p.Post(id=0,title="title",date=datetime.date(2021,1,1),path="/post.post")])
        )

    def test_load_missing_parameter(self):
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'title':'title',
                'public':False,
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':0,
                'public':False,
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':0,
                'title':'title',
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':0,
                'title':'title',
                'public':False,
            },'/project/')

    def test_load_type_errors(self):
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':'abc',
                'title':'title',
                'public':False,
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':'0',
                'title':'title',
                'public':'abc',
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':'0',
                'title':'title',
                'public':False,
                'posts':'abc'
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':'0',
                'title':'title',
                'public':'',
                'posts':[]
            },'/project/')
        with self.assertRaises(ValueError):
            pr.Project.load_project({
                'id':'0',
                'title':'title',
                'public':'True',
                'posts':[]
            },'/project/')

    def test_write(self):
        self.assertEqual(
            pr.Project(path="/project/",id=0,title="title",public=False,posts=[]).write(),
            {
                'id':0,
                'title':'title',
                'public':False,
                'posts':[]
            }
        )
        self.assertEqual(
            pr.Project(path="abc",id=-5001,title='',public=True,posts=[p.Post(id=0,title="title",date=datetime.date(2021,1,1),path="/post.post")]).write(),
            {
                'id':-5001,
                'title':'',
                'public':True,
                'posts': [
                    {
                    "id":"0",
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post"
                    }]
            }
        )


if __name__ == '__main__':
    unittest.main()