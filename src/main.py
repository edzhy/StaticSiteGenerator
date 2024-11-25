from textnode import *
from htmlnode import HTMLNode

def main():
    dummy_TextNode = TextNode(text='this is a test', text_type=TextType.IMAGE, url='https://www.boot.dev')
    print(dummy_TextNode.text_node_to_html_node().to_html())
    print(dummy_TextNode.__repr__())
    dummy_HTMLNode = HTMLNode(tag='a',value='test', children=None, props={'href':'google.com', 'href2':'google.net'})
    print(dummy_HTMLNode.__repr__())
    print(dummy_HTMLNode.props_to_html())

if __name__ == "__main__":
    main()