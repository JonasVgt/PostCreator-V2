import datetime
import json
import package.post as p
import unittest

class TestPostEncoder(unittest.TestCase):
    

    def test_encode(self):
        self.assertEqual(
            json.dumps(p.Post(id=0,title="title",date=datetime.date(2021,1,1),path="/post.post",public=True)),
            """{
                "id":0,
                "title":"title",
                "date":"2021-01-01",
                "path":"/post.post",
                "public":True
            }"""
        )
        # self.assertEqual(
        #     p.Post(id=-5005,title="",date=datetime.date(2001,3,2),path="/home/post.post",public=False).write(),
        #     {
        #         "id":-5005,
        #         "title":"",
        #         "date":"2001-03-02",
        #         "path":"/home/post.post",
        #         "public":False
        #     }
        # )



if __name__ == '__main__':
    unittest.main()