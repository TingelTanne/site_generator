class HTMLNode():
    def __init__(self, tag = None, value = None, children = None , props = None):
        self.tag = tag
        self.value = value
        self.children = children      
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        children_repr = None if not self.children else self.children
        return f"HTMLNode({self.tag}, {self.value}, children: {children_repr}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError ("All leaf nodes must have a value")
        if self.tag == None:
            return str(self.value)
                
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNodes must have a tag")
        if not children or len(children) == 0:
            raise ValueError("ParentNodes must have at least one ChildNode")
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        child_str = ""
        for child in self.children:
            child_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_str}</{self.tag}>"
