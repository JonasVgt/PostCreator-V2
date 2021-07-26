import package.parser.document_parser as p
import package.errors as e
import unittest

class TestParserList(unittest.TestCase):

    def test_list(self):
        self.assertEqual(p.DocumentParser("This is a \\list{\\item a \\item b \\item c } String",0).parse(),"<p>This is a <ul><li>a </li><li>b </li><li>c </li></ul> String</p>")
    
    def test_list_space(self):
        self.assertEqual(p.DocumentParser("This is a \\list{   \\item a \\item b \\item c } String",0).parse(),"<p>This is a <ul><li>a </li><li>b </li><li>c </li></ul> String</p>")


    def test_list_no_item(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\list{wrong\\item a \\item b \\item c} String",0).parse()

    def test_list_tag(self):
        self.assertEqual(p.DocumentParser("This is a \\list{   \\item a \\item \\em{b} \\item c } String",0).parse(),"<p>This is a <ul><li>a </li><li><em>b</em> </li><li>c </li></ul> String</p>")

    def test_list_encapsulated_item(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\list{wrong\\item a \\item \\em{b \\item c}} String",0).parse()

if __name__ == '__main__':
    unittest.main()
