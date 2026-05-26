import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    node = HTMLNode(
        tag="div",
        value="Hello",
        children=[HTMLNode(tag="span", value="World")],
        props={"class": "test", "id": "test-id"},
    )

    def test_repr(self):
        self.assertEqual(
            self.node.__repr__(),
            f"<{self.node.tag} {self.node.props_to_html()}> {self.node.value}, {self.node.children} </{self.node.tag}>",
        )

    def test_props_to_html(self):
        self.assertEqual(self.node.props_to_html(), " class='test' id='test-id'")

    def test_to_html(self):
        try:
            self.node.to_html()
        except Exception as e:
            self.assertEqual(isinstance(e, NotImplementedError), True)


class TestLeafNode(unittest.TestCase):
    P_Node = LeafNode(tag="p", value="This is a paragraph of text.")
    A_Node = LeafNode(tag="a", value="Link", props={"href": "https://example.com"})

    def test_p_Node(self):
        self.assertEqual(self.P_Node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_a_Node(self):
        self.assertEqual(
            self.A_Node.to_html(), "<a href='https://example.com'>Link</a>"
        )

    def test_A_props_to_html(self):
        self.assertEqual(self.A_Node.props_to_html(), " href='https://example.com'")

    def test_p_Node_props_to_html(self):
        self.assertEqual(self.P_Node.props_to_html(), "")


class TestparentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multpul_children(self):
        child1 = LeafNode(tag="b", value="child1")
        child2 = LeafNode(tag="t", value="child2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child1</b><t>child2</t></div>",
        )

    def test_to_html_value_error(self):
        parent_node = ParentNode("div")
        try:
            parent_node.to_html()
        except Exception as e:
            self.assertEqual(isinstance(e, ValueError), True)
