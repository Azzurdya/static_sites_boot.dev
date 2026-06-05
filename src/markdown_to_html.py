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
        return ParentNode("h1", children=html_nodes)
    elif type == "code":
        return ParentNode("pre", children=html_nodes)
    elif type == "quote":
        return ParentNode("blockquote", children=html_nodes)
    elif type == "unordered_list":
        return ParentNode("ul", children=html_nodes)
    elif type == "ordered_list":
        return ParentNode("ol", children=html_nodes)

    else:
        return html_nodes


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
this should be code **and not bold**
```

- item 1
- item 2
- item 3

1. item 1
2. item 2
3. item 3

1. item 1
3. item 3
2. item 2
"""
print(markdown_to_html_node(md))
