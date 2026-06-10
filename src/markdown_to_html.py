import re

import textnode
import TextToBlock
import TextToTextNode
from htmlnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = TextToBlock.markdown_to_blocks(markdown)

    type = [TextToBlock.block_to_type(block) for block in blocks]

    nodes = []
    for block in blocks:
        nodes.append(TextToTextNode.text_to_textnodes(block))

    html_paragraph = []
    for i in range(len(nodes)):
        html_paragraph.append(
            parent_wrapper(markdown_block_to_html_node(nodes[i], type[i]), type[i])
        )
    return ParentNode("div", children=html_paragraph).to_html()


def markdown_block_to_html_node(block, type):
    html_nodes = []
    for node in block:
        if type == "unordered_list" or type == "ordered_list":
            return textnode.text_node_to_html_node(node)
        html_nodes.append(textnode.text_node_to_html_node(node))
    return html_nodes


def parent_wrapper(html_nodes, type):
    if type == "paragraph":
        return ParentNode("p", children=html_nodes)
    elif type == "heading":
        nums = html_nodes[0].value.count("#")
        html_nodes[0].value = html_nodes[0].value.lstrip("#")
        return ParentNode(f"h{nums}", children=html_nodes)
    elif type == "code":
        return ParentNode("pre", children=html_nodes)
    elif type == "quote":
        html_nodes[0].value = re.sub(r">", "", html_nodes[0].value)
        return ParentNode("blockquote", children=html_nodes)
    elif type == "unordered_list":
        return ParentNode("ul", children=html_nodes)
    elif type == "ordered_list":
        return ParentNode("ol", children=html_nodes)

    else:
        return html_nodes


# md = """
# title 1

## heading 2

## # invalid heading

# """

# print(markdown_to_html_node(md))
