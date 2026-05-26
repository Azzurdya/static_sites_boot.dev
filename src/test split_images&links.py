import unittest

import Split_Images_and_Links
import textnode


class TestSplitImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = textnode.Textnode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            textnode.Texttype["Plain"],
        )
        new_nodes = Split_Images_and_Links.split_nodes_image([node])
        self.assertListEqual(
            [
                textnode.Textnode("This is text with an ", textnode.Texttype["Plain"]),
                textnode.Textnode(
                    "image",
                    textnode.Texttype["Image"],
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                textnode.Textnode(" and another ", textnode.Texttype["Plain"]),
                textnode.Textnode(
                    "second image",
                    textnode.Texttype["Image"],
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

        def test_split_link(self):
            node = textnode.Textnode(
                "This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/second)",
                textnode.Texttype["Plain"],
            )
            new_nodes = Split_Images_and_Links.split_nodes_link([node])
            self.assertListEqual(
                [
                    textnode.Textnode(
                        "This is text with a ", textnode.Texttype["Plain"]
                    ),
                    textnode.Textnode(
                        "link",
                        textnode.Texttype["Link"],
                        "https://www.example.com",
                    ),
                    textnode.Textnode(" and another ", textnode.Texttype["Plain"]),
                    textnode.Textnode(
                        "second link",
                        textnode.Texttype["Link"],
                        "https://www.example.com/second",
                    ),
                ],
                new_nodes,
            )
