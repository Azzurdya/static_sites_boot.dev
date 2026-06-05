from pickletools import markobject

import delimiter
import Split_Images_and_Links
import textnode
from TextToBlock import block_to_type


def text_to_textnodes(Text):
    type = block_to_type(Text)
    if type == "unordered_list":
        return [textnode.Textnode(Text, textnode.Texttype["Unordered_List"])]
    elif type == "ordered_list":
        return [textnode.Textnode(Text, textnode.Texttype["Ordered_List"])]
    else:
        markdown_text = [textnode.Textnode(Text, textnode.Texttype["Plain"])]
        New_TextNodes = delimiter.split_nodes_delimiter(
            markdown_text, "`", textnode.Texttype["Code"]
        )
        New_TextNodes = delimiter.split_nodes_delimiter(
            New_TextNodes, "**", textnode.Texttype["Bold"]
        )
        New_TextNodes = delimiter.split_nodes_delimiter(
            New_TextNodes, "_", textnode.Texttype["Italic"]
        )

        New_TextNodes = Split_Images_and_Links.split_nodes_image(New_TextNodes)
        New_TextNodes = Split_Images_and_Links.split_nodes_link(New_TextNodes)
        return New_TextNodes


# markdown_node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


# print(text_to_textnodes(markdown_node))
