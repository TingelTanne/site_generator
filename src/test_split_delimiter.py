import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    
    def test_to_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_italic_text(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ]
        )
        
    def test_multiple_delimiters(self):
        node = TextNode("This has `code` and **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_non_text_nodes_unchanged(self):
        """Test that non-text nodes are left unchanged."""
        node = TextNode("This is bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_multiple_occurrences(self):
        """Test handling multiple occurrences of the same delimiter."""
        node = TextNode("Text with `code1` and `code2` blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode(" blocks", TextType.TEXT),
            ]
        )

    def test_adjacent_delimiters(self):
        """Test handling adjacent delimited sections."""
        node = TextNode("**Bold**_italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
            ]
    )

    def test_mixed_node_list(self):
        """Test with a mixed list of node types."""
        nodes = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("existing bold", TextType.BOLD),
            TextNode(" and `code` to find", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("existing bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" to find", TextType.TEXT),
            ]
        )

    def test_missing_closing_delimiter(self):
        """Test that an exception is raised when a closing delimiter is missing."""
        node = TextNode("Text with `code but no closing tick", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()