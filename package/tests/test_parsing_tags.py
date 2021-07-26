import package.parser.document_parser as p
import unittest

class TestParserTags(unittest.TestCase):

    def test_tag_em(self):
        self.assertEqual(p.DocumentParser("This is a \\em{test} String",0).parse(),"<p>This is a <em>test</em> String</p>")

    def test_tag_st(self):
        self.assertEqual(p.DocumentParser("This is a \\st{test} String",0).parse(),"<p>This is a <strong>test</strong> String</p>")

    def test_tag_simple_insert(self):
        self.assertEqual(p.DocumentParser("This is a \\curly_right test String",0).parse(),"<p>This is a &#x7D; test String</p>")

    def test_tag_simple_insert_bracket(self):
        self.assertEqual(p.DocumentParser("This is a \\{curly_right}test String",0).parse(),"<p>This is a &#x7D;test String</p>")

    

if __name__ == '__main__':
    unittest.main()
