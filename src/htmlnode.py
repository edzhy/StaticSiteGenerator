class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ''
        for key, value in self.props.items():
            result += ' ' + key + '="' + value +'"'
        return result
    
    def __eq__(self, HTMLNode):
        return (
            (self.tag == HTMLNode.tag) and 
            (self.value == HTMLNode.value) and 
            (self.children == HTMLNode.children) and
            (self.props == HTMLNode.props)
        )

    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
