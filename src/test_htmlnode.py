import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_with_single_child(self):
        child = LeafNode("b", "Bold text")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(),
            "<div><b>Bold text</b></div>"
        )

    def test_to_html_with_nested_nodes(self):
        leaf1 = LeafNode("b", "Bold text")
        leaf2=LeafNode(None, "Normal text")
        child_parent = ParentNode("div", [leaf1, leaf2])
        grand_parent = ParentNode("section", [child_parent])
        self.assertEqual(
            grand_parent.to_html(),
            "<section><div><b>Bold text</b>Normal text</div></section>",
        )

if __name__ == "__main__":
    unittest.main()
