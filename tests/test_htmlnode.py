import unittest

from src.htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
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


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_value_is_None(self):
        node = LeafNode("b", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_tag_is_None(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
