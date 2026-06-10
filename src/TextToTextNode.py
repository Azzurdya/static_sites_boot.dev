import re
from pickletools import markobject

import delimiter
import Split_Images_and_Links
import textnode
from TextToBlock import block_to_type


def text_to_textnodes(Text):
    type = block_to_type(Text)
    if type == "unordered_list":
        list = Text.split("\n")
        childern = []
        for line in list:
            line = re.sub(r"^- ", "", line, re.M)
            line = text_to_textnodes(line)
            childern.append(line)
        return [textnode.Textnode(childern, textnode.Texttype["Unordered_List"])]

    elif type == "ordered_list":
        list = Text.split("\n")
        childern = []
        for line in list:
            line = re.sub(r"\d.", "", line, re.M)
            line = text_to_textnodes(line)
            childern.append(line)
        return [textnode.Textnode(childern, textnode.Texttype["Ordered_List"])]
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
