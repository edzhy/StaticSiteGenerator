import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_split_code_block(self):
        """Test splitting of text nodes using the CODE delimiter."""
        nodes = [TextNode("This is a `code block` and some text.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        # Verify the split result
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].text_type, 'text')
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, 'code')
        self.assertEqual(result[2].text, " and some text.")
        self.assertEqual(result[2].text_type, 'text')
    
    def test_unbalanced_code_delimiter(self):
        """Test unbalanced delimiters for CODE."""
        nodes = [TextNode("This is a `code block and some text.", TextType.TEXT)]
        
        # Expecting an exception due to unbalanced delimiters
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "`", TextType.CODE)
        
        self.assertEqual(str(context.exception), 'The initial input contains invalid Markdown syntax')

if __name__ == '__main__':
    unittest.main()