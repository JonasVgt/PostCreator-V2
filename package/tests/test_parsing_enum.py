import package.parser.document_parser as p
import package.errors as e
import unittest

class TestParserEnum(unittest.TestCase):

    def test_enum(self):
        self.assertEqual(p.DocumentParser("This is a \\enum{\\item a \\item b \\item c } String",0).parse(),"<p>This is a <ol><li>a </li><li>b </li><li>c </li></ol> String</p>")
    
    def test_enum_space(self):
        self.assertEqual(p.DocumentParser("This is a \\enum{   \\item a \\item b \\item c } String",0).parse(),"<p>This is a <ol><li>a </li><li>b </li><li>c </li></ol> String</p>")


    def test_enum_no_item(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\enum{wrong\\item a \\item b \\item c} String",0).parse()

    def test_enum_tag(self):
        self.assertEqual(p.DocumentParser("This is a \\enum{   \\item a \\item \\em{b} \\item c } String",0).parse(),"<p>This is a <ol><li>a </li><li><em>b</em> </li><li>c </li></ol> String</p>")

    def test_enum_encapsulated_item(self):
        with self.assertRaises(e.ParseError):
            p.DocumentParser("This is a \\enum{wrong\\item a \\item \\em{b \\item c}} String",0).parse()

if __name__ == '__main__':
    unittest.main()
