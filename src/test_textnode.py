import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()