import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('this is a test', tag='p')
        self.assertEqual(node.to_html(), ("<p>this is a test</p>"))
    
    def test_eq1(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_params(self):
        node = LeafNode(value='this is a test', tag=None)
        self.assertEqual(node.to_html(), 'this is a test')