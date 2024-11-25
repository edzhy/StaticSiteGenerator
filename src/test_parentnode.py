import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
    tag="p",
    children=[
        LeafNode(tag="b", value="Bold text"),
        LeafNode(tag=None, value="Normal text"),
        LeafNode(tag="i", value="italic text"),
        LeafNode(tag=None, value="Normal text"),
    ],
    )

        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_nestedParent(self):
        ultra_node = ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
            ParentNode(
                tag='ol',
                children=[
                    LeafNode(tag='li', value='first item'),
                    LeafNode(tag='li', value='second item')
                ]
            )
        ],
        )
        self.assertEqual(ultra_node.to_html(),
                         '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<ol><li>first item</li><li>second item</li></ol></p>')
        