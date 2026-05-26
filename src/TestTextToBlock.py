import unittest

import TextToBlock


class TestTextToBlock(unittest.TestCase):
    markdown_text = """# Heading 1\n\nThis is a paragraph.\n\n```python
print('Hello, world!')
```\n\n> This is a quote.\n> it has two parts\n\n- Unordered item 1\n- Unordered item 2\n\n1. Ordered item 1\n2. Ordered item 2"""

    def test_text_to_blocks(self):
        blocks = TextToBlock.markdown_to_blocks(self.markdown_text)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "This is a paragraph.",
                "```python\nprint('Hello, world!')\n```",
                "> This is a quote.\n> it has two parts",
                "- Unordered item 1\n- Unordered item 2",
                "1. Ordered item 1\n2. Ordered item 2",
            ],
        )

    def test_is_valid_ordered_list(self):
        self.assertTrue(TextToBlock.is_valid_ordered_list("1. Item 1\n2. Item 2"))
        self.assertFalse(
            TextToBlock.is_valid_ordered_list("1. Item 1\n3. Item 2")
        )  # Invalid because of line 2

    def test_block_type(self):
        blocks = TextToBlock.markdown_to_blocks(self.markdown_text)
        result = [TextToBlock.block_to_type(block) for block in blocks]
        self.assertEqual(
            result,
            ["heading", "paragraph", "code", "quote", "unordered_list", "ordered_list"],
        )


if __name__ == "__main__":
    unittest.main()
