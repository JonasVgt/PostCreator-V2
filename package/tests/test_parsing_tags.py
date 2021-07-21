import package.parser.document_parser as p
import unittest

class TestParserTags(unittest.TestCase):

    def test_tag_em(self):
        self.assertEqual(p.DocumentParser("This is a \\em{test} String",0).parse(),"This is a <em>test</em> String")

    def test_tag_st(self):
        self.assertEqual(p.DocumentParser("This is a \\st{test} String",0).parse(),"This is a <strong>test</strong> String")


 
if __name__ == '__main__':
    unittest.main()
