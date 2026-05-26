import unittest

from regex_image_text_extract import extract_markdown_images, extract_markdown_links


class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](image.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "image.jpg")])

    def test_extract_markdown_links(self):
        text = "[link text](http://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link text", "http://example.com")])


if __name__ == "__main__":
    unittest.main()
