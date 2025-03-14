from src.htmlnode import HTMLNode


def main():
    anchor_node = HTMLNode(
        tag="a", props={"href": "https://www.google.com", "target": "_blank"}
    )
    print(anchor_node)


if __name__ == "__main__":
    main()
