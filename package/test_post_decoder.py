import datetime
import package.post as p
import unittest

class TestPostEncoder(unittest.TestCase):
    
    def test_read(self):
        self.assertEqual(
            p.Post.read_post(
                {
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":False
                }),
            p.Post(id=0,title="title",date=datetime.date(2021,1,1),path="/post.post",public=False)
        )
        self.assertEqual(
            p.Post.read_post(
                {
                    "id":-5005,
                    "title":"",
                    "date":"2001-03-02",
                    "path":"/home/post.post",
                    'public':True
                }),
            p.Post(id=-5005,title="",date=datetime.date(2001,3,2),path="/home/post.post",public=True)
        )

    def test_read_missing_parameter(self):
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "path":"/post.post",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post"
                })

    def test_read_type_errors(self):
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":"abc",
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"abc",
                    "path":"/post.post",
                    "public":False
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":"abc"
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":""
                })
        with self.assertRaises(ValueError):
            p.Post.read_post({
                    "id":0,
                    "title":"title",
                    "date":"2021-01-01",
                    "path":"/post.post",
                    "public":"True"
                })

    def test_write(self):
        self.assertEqual(
            p.Post(id=0,title="title",date=datetime.date(2021,1,1),path="/post.post",public=True).write(),
            {
                "id":0,
                "title":"title",
                "date":"2021-01-01",
                "path":"/post.post",
                "public":True
            }
        )
        self.assertEqual(
            p.Post(id=-5005,title="",date=datetime.date(2001,3,2),path="/home/post.post",public=False).write(),
            {
                "id":-5005,
                "title":"",
                "date":"2001-03-02",
                "path":"/home/post.post",
                "public":False
            }
        )



if __name__ == '__main__':
    unittest.main()