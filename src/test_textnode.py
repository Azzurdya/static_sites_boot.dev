import unittest

from htmlnode import *
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", Texttype["Bold"])
        node2 = Textnode("This is a text node", Texttype["Bold"])
        self.assertEqual(node, node2)

    def test_ne(self):
        node = Textnode("This is a text node", Texttype["Bold"])
        node2 = Textnode("This is a text node", Texttype["Italic"])
        self.assertNotEqual(node, node2)

    def test_link(self):
        node = Textnode("This is a text node", Texttype["Bold"], "https://example.com")
        self.assertEqual(node.link, "https://example.com")

    def test_no_link(self):
        node = Textnode("This is a text node", Texttype["Bold"])
        self.assertIsNone(node.link)

    def test_text_there(self):
        node = Textnode("This is a text node", Texttype["Bold"])
        self.assertTrue(node.text)

    def TEXT_TO_HTML_test_text(self):
        node = Textnode("This is a text node", Texttype["Plain"])
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def TEXT_TO_HTML_test_bold(self):
        node = Textnode("This is a text node", Texttype["Bold"])
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def TEXT_TO_HTML_test_italic(self):
        node = Textnode("This is a text node", Texttype["Italic"])
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def TEXT_TO_HTML_test_link(self):
        node = Textnode("This is a text node", Texttype["Bold"], "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def TEXT_TO_HTML_test_code(self):
        node = Textnode("This is a text node", Texttype["Code"])
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def TEXT_TO_HTML_test_img(self):
        node = Textnode(
            "This is a text node", Texttype["Image"], "https://example.com/image.jpg"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/image.jpg", "alt": "This is a text node"},
        )

    def TEXT_TO_HTML_test_(self):
        node = Textnode("This is a text node", Texttype[""])
        try:
            html_node = text_node_to_html_node(node)
        except ValueError:
            pass
        else:
            self.fail("Expected ValueError for unknown text type")


if __name__ == "__main__":
    unittest.main()
