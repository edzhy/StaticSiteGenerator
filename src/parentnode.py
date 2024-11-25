from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag, props=None):
        if tag is None:
            raise ValueError('ParentNode requires tag argument')
        if not isinstance(children, list) or not children:
            raise ValueError("Children' argument requires a non-empty list")

        super().__init__(children=children, tag=tag, props=props)

    def to_html(self):
        return f"<{self.tag}>{self.recursive_children()}</{self.tag}>"
    
    def recursive_children(self): #PLEASE CREATE A CHECK IF THERE IS A NESTED PARENT, AND IF SO DEAL WITH THAT PARENT FIRST
        if len(self.children) == 1:
            #if isinstance(self.children[0], ParentNode):
            return self.children[0].to_html()
        else:
            return self.children[0].to_html() + ParentNode(tag=self.tag,children=self.children[1:]).recursive_children()
        
    #create __eq__ method for this call
    def __eq__(self, ParentNode):
        return (
            (self.tag == ParentNode.tag) and
            (self.children == ParentNode.children) and
            (self.props == ParentNode.props)
        )
    #create __repr__ method
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
