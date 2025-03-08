import unittest
from extractors import *

class TestExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Test with multiple images
        test_image = "Here's an image ![cute cat](https://example.com/cat.jpg) and another ![dog photo](https://example.com/dog.png)"
        expected = [('cute cat', 'https://example.com/cat.jpg'), ('dog photo', 'https://example.com/dog.png')]
        self.assertEqual(extract_markdown_images(test_image), expected)
        
        # Test with no images
        no_images = "This text has no markdown images"
        self.assertEqual(extract_markdown_images(no_images), [])
        
        # Test with the example from the lesson
        lesson_example = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(lesson_example), expected)
    
    def test_extract_markdown_links(self):
        # Test with multiple links
        test_link = "Check out [this website](https://example.com) and [another site](https://another-example.org)"
        expected = [('this website', 'https://example.com'), ('another site', 'https://another-example.org')]
        self.assertEqual(extract_markdown_links(test_link), expected)
        
        # Test with no links
        no_links = "This text has no markdown links"
        self.assertEqual(extract_markdown_links(no_links), [])
        
        # Test with the example from the lesson
        lesson_example = "This is text with a link [to boot dev](https://www.boot.dev)"


if __name__ == "__main__":
    unittest.main()
