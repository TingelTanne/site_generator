import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different node", TextType.BOLD)
        node4 = TextNode("This is a different node", TextType.ITALIC)
        urlNode = TextNode("This is a text node", TextType.BOLD, url="google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node, urlNode)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        # Create a TextNode with type LINK - typically links have text and a URL
        node = TextNode("Click me", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        
        # Check that we got the right tag (a), value (the anchor text), 
        # and href property (the URL)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://example.com")

    def test_image(self):
        # Create a TextNode with type IMAGE - typically images have alt text and a URL
        node = TextNode("Alt text for image", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        
        # Check that we got the right tag (img), empty value, and both src and alt properties
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Image nodes have empty value
        self.assertEqual(html_node.props["src"], "https://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "Alt text for image")

if __name__ == "__main__":
    unittest.main()