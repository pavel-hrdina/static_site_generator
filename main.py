from src.htmlnode import ParentNode, LeafNode


def main():
    node = ParentNode(
        "p",
        [
            LeafNode(tag="b", value="Bold text"),
            LeafNode(tag=None, value="Normal text"),
            LeafNode(tag="i", value="italic text"),
            LeafNode(tag=None, value="Normal text"),
        ],
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
