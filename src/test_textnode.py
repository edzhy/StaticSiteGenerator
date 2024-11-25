import unittest 
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is not a node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_image(self):
        node = TextNode(text='this is a test', text_type=TextType.IMAGE, url='https://www.boot.dev')
        self.assertEqual(node.text_node_to_html_node().to_html(), '<img src="https://www.boot.dev" alt="this is a test">')

    def test_bold(self):
        node = TextNode(text='this is a test', text_type=TextType.BOLD)
        sub_result = node.text_node_to_html_node()
        self.assertEqual(sub_result.to_html(), '<b>this is a test</b>')

if __name__ == "__main__":
    unittest.main()