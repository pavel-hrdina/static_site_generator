import unittest

from src.htmlnode import (
    HTMLNode,
    LeafNode,
)  # Assuming the HTMLNode class is in the src directory


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        """Test if props_to_html handles an empty props dictionary correctly."""
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_property(self):
        """Test if props_to_html handles a single property correctly."""
        node = HTMLNode(tag="a", props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com"')

    def test_props_to_html_multiple_properties(self):
        """Test if props_to_html handles multiple properties correctly."""
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.example.com",
                "target": "_blank",
                "class": "btn",
            },
        )
        expected = 'href="https://www.example.com" target="_blank" class="btn"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_value_is_None(self):
        node = LeafNode(None, "Hello, world!")
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_tag_is_None(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
