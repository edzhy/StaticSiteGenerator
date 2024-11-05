from textnode import *

def main():
    dummy_TextNode = TextNode('this is a test', TextType.BOLD, 'https://www.boot.dev')
    print(dummy_TextNode.__repr__())

if __name__ == "__main__":
    main()