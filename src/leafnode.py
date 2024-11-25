from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value=value, tag=tag, props=props)
        #self.value = value

    def to_html(self):
        
        if self.value == None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    #create __eq__ method for this call
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (
            self.value == other.value and
            self.tag == other.tag and
            self.props == other.props
        )
    #create __repr__ method
    def __repr__(self):
        return f'LeafNode({self.value}, {self.tag}, {self.props})'