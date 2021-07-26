import package.parser.document_parser as p
import unittest
class TestTagParser(unittest.TestCase):

    def test_notags(self):
        self.assertEqual(p.DocumentParser("This is a test String",0).parse(),"<p>This is a test String</p>")

    def test_tag_at_end(self):
        self.assertEqual(p.DocumentParser("This is a test \\em{String}",0).parse(),"<p>This is a test <em>String</em></p>")

    def test_tag_at_beginning(self):
        self.assertEqual(p.DocumentParser("\\em{This} is a test String",0).parse(),"<p><em>This</em> is a test String</p>")

    def test_tag_whole_input(self):
        self.assertEqual(p.DocumentParser("\\em{This is a test String}",0).parse(),"<p><em>This is a test String</em></p>")

    def test_multiple_different_tags(self):
        self.assertEqual(p.DocumentParser("\\em{This} is \\st{a} \\em{test} String",0).parse(),"<p><em>This</em> is <strong>a</strong> <em>test</em> String</p>")

    def test_multiple_same_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is} \\em{a} \\em{test} String",0).parse(),"<p>This <em>is</em> <em>a</em> <em>test</em> String</p>")

    def test_layered_same_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is \\em{a} \\em{test}} String",0).parse(),"<p>This <em>is <em>a</em> <em>test</em></em> String</p>")

    def test_layered_different_tags(self):
        self.assertEqual(p.DocumentParser("This \\em{is \\em{a} \\st{test}} String",0).parse(),"<p>This <em>is <em>a</em> <strong>test</strong></em> String</p>")

    def test_paragraphs(self):
        self.assertEqual(p.DocumentParser("This \\em{is} \\em{a}\\p \\em{test}\\p String",0).parse(),"<p>This <em>is</em> <em>a</em></p><p> <em>test</em></p><p> String</p>")


if __name__ == '__main__':
    unittest.main()
