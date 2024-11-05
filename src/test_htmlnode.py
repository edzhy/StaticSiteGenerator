import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(tag='a',value=None, children=None, props=None)
        node2 = HTMLNode(tag='a',value=None, children=None, props=None)
        self.assertEqual(node1, node2)

    def raiseNotImplemented(self):
        node1 = HTMLNode('a',value='test', children=None, props={'href':'google.com'})
        node1.to_html()
            
    def test_ineq(self):
        node1 = HTMLNode(tag='a',value=None, children=None, props=None)
        node2 = HTMLNode('a',value='test', children=None, props={'href':'google.com'})
        self.assertNotEqual(node1, node2)

    def test_self(self):
        node = HTMLNode('div', 'how to center a div', props={'magnificent':'Edgars'})
        self.assertEqual(
            node.tag,
            'div'
        )
        self.assertEqual(
            node.value,
            'how to center a div'
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {'magnificent':'Edgars'}
        )

if __name__ == "__main__":
    unittest.main()