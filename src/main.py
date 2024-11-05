from textnode import *
from htmlnode import HTMLNode

def main():
    dummy_TextNode = TextNode('this is a test', TextType.BOLD, 'https://www.boot.dev')
    #dummy_TextNode = TextNode('this is a test', TextType.BOLD)
    print(dummy_TextNode.__repr__())
    dummy_HTMLNode = HTMLNode('a',value='test', children=None, props={'href':'google.com', 'href2':'google.net'})
    print(dummy_HTMLNode.__repr__())
    print(dummy_HTMLNode.props_to_html())
if __name__ == "__main__":
    main()