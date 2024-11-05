from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url
    
    def __eq__(self,TextNode):
        return (
            (self.text == TextNode.text) and
            (self.text_type == TextNode.text_type) and
            (self.url == TextNode.url)
        )
    def __repr__(self):
        text, text_type, url = str(self.text), str(self.text_type), str(self.url)
        return f'TextNode({text}, {text_type}, {url})'