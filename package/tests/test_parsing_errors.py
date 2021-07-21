import package.parser.document_parser as p
import unittest
import package.errors as e

class TestParserErrors(unittest.TestCase):

    def test_undefined_tag_bracket(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\unknownTag{test} String",0).parse()

    def test_undefined_tag_space(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\unknownTag test String",0).parse()
    
    def test_bracket_not_closed(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\em{test String",0).parse()

    def test_unbalanced_brackets(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is \\em{a \\em{test} String",0).parse()



    def test_lost_special_curly_bracket_open(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This {is a \\em{test} String",0).parse()

    def test_lost_bracket_curly_bracket_closed(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This }is a \\em{test} String",0).parse()

    def test_empty_tag_bracket(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\{test} String",0).parse()

    def test_empty_tag_space(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\ test String",0).parse()


if __name__ == '__main__':
    unittest.main()
