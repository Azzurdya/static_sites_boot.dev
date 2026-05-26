from enum import Enum

from htmlnode import LeafNode

Texttype = {
    "Plain": "Plain",
    "Bold": "Bold",
    "Italic": "Italic",
    "Code": "Code",
    "Link": "Link",
    "Image": "Image",
}


class Textnode:
    def __init__(self, text, texttype, link=None):
        self.text = text
        self.link = link
        self.texttype = texttype

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.texttype == other.texttype
            and self.link == other.link
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.texttype}, {self.link})"


def text_node_to_html_node(text_node):
    if text_node.texttype == "Plain":
        return LeafNode(value=text_node.text)
    elif text_node.texttype == "Bold":
        return LeafNode(text_node.text, tag="b")
    elif text_node.texttype == "Italic":
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.texttype == "Code":
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.texttype == "Link":
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.link})
    elif text_node.texttype == "Image":
        return LeafNode(
            value="", tag="img", props={"src": text_node.link, "alt": text_node.text}
        )
    else:
        raise ValueError(f"Unknown text type: {text_node.texttype}")
