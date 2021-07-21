import package.parser.document_parser as p
import unittest
class TestTagParser(unittest.TestCase):

    def test_notags(self):
        self.assertEqual(p.DocumentParser("This is a test String",0).parse(),"This is a test String")

    def test_tag_at_end(self):
        self.assertEqual(p.DocumentParser("This is a test \\em{String}",0).parse(),"This is a test <em>String</em>")

    def test_tag_at_beginning(self):
        self.assertEqual(p.DocumentParser("\\em{This} is a test String",0).parse(),"<em>This</em> is a test String")

    def test_tag_whole_input(self):
        self.assertEqual(p.DocumentParser("\\em{This is a test String}",0).parse(),"<em>This is a test String</em>")

    def test_multiple_different_tags(self):
        self.assertEqual(p.DocumentParser("\\em{This} is \\st{a} \\em{test} String",0).parse(),"<em>This</em> is <strong>a</strong> <em>test</em> String")

    def test_multiple_same_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is} \\em{a} \\em{test} String",0).parse(),"This <em>is</em> <em>a</em> <em>test</em> String")

    def test_layered_same_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is \\em{a} \\em{test}} String",0).parse(),"This <em>is <em>a</em> <em>test</em></em> String")

    def test_layered_different_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is \\em{a} \\st{test}} String",0).parse(),"This <em>is <em>a</em> <strong>test</strong></em> String")


if __name__ == '__main__':
    unittest.main()
