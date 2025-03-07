from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    
    def __init__(self, text, text_type:TextType, url = None):
        if not isinstance(text_type, TextType):
            raise ValueError(f"Invalid text_type: {text_type}. Must be a TextType enum value.")
        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.LINK:
        html_node = LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        html_node = LeafNode("img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        html_node = LeafNode(text_node.text_type.value, text_node.text)
    return html_node
