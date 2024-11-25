from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        if text_type in TextType:
            self.text = text
            self.text_type = text_type.value
            self.url = url
        else:
            raise ValueError('Not a valid attribute entered for TextType class')
    
    def __eq__(self,TextNode):
        return (
            (self.text == TextNode.text) and
            (self.text_type == TextNode.text_type) and
            (self.url == TextNode.url)
        )
    def __repr__(self):
        text, text_type, url = str(self.text), str(self.text_type), str(self.url)
        return f'TextNode({text}, {text_type}, {url})'
    
    def text_node_to_html_node(self):
        match self.text_type:
            case "text":
                return LeafNode(self.text)
            case "bold":
                return LeafNode(self.text,tag='b')
            case "italic":
                return LeafNode(self.text,tag='i')
            case "code":
                return LeafNode(self.text,tag='code')
            case "link":
                #This is a paragraph with a <a href="https://www.google.com">link</a>.
                return LeafNode(self.text,tag='a', props={'href':self.url})
            case "image":
                #<img src="url/of/image.jpg" alt="Description of image">
                return LeafNode(value='',tag="img", props={'src':self.url, 'alt':self.text})