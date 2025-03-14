from typing import Optional, Dict, List


class HTMLNode:
    """Represents an HTML node"""

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Transform this node into HTML"""
        raise NotImplementedError()

    def props_to_html(self) -> str:
        """Generate HTML attribute string from the 'props' dictionary."""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self) -> str:
        """Prints 'HTMLNode' object and its children."""
        # Ensure children is iterable, and avoid issues if it contains non-HTMLNode objects
        children_repr = (
            [repr(child) for child in self.children]
            if isinstance(self.children, list)
            else []
        )
        return (
            f"HTMLNode(tag={repr(self.tag)}, "
            f"value={repr(self.value)}, "
            f"children={children_repr}, "
            f"props={repr(self.props)})"
        )


class LeafNode(HTMLNode):
    """Represents an HTML leaf node"""

    def __init__(
        self,
        value: str | None,
        tag: Optional[str] = None,
    ):
        super().__init__(tag, value)
        self.value = value
        if self.children:
            raise ValueError("LeafNode cannot have children")

    def to_html(self):
        """Transforms values to HTML. Value and tag must be explicitly defined, when the object is created."""
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return f"{self.value}"

        return f"<{self.tag}>{self.value}</{self.tag}>"
