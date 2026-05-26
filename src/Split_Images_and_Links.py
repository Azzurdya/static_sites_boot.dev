import re

import regex_image_text_extract
import textnode


def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.texttype != textnode.Texttype["Plain"]:
            nodes.append(node)
            continue

        text = node.text
        image_nodes = []
        current_string = text
        # text_nodes = re.findall(r"\b\w+\b(?![^\[]*\])(?![^\(]*\))", text)
        image_nodes = regex_image_text_extract.extract_markdown_images(text)

        if len(image_nodes) == 0:
            nodes.append(node)
            continue

        for image in image_nodes:
            current_string = current_string.split(f"![{image[0]}]({image[1]})", 1)
            if current_string[0] != "":
                nodes.append(
                    textnode.Textnode(current_string[0], textnode.Texttype["Plain"])
                )
            nodes.append(
                textnode.Textnode(
                    text=image[0], texttype=textnode.Texttype["Image"], link=image[1]
                )
            )
            current_string = current_string[1]
        if current_string != "":
            nodes.append(textnode.Textnode(current_string, textnode.Texttype["Plain"]))
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.texttype != textnode.Texttype["Plain"]:
            nodes.append(node)
            continue

        text = node.text
        link_nodes = []
        current_string = text
        # text_nodes = re.findall(r"\b\w+\b(?![^\[]*\])(?![^\(]*\))", text)
        link_nodes = regex_image_text_extract.extract_markdown_links(text)

        if len(link_nodes) == 0:
            nodes.append(node)
            continue

        for link in link_nodes:
            current_string = current_string.split(f"[{link[0]}]({link[1]})", 1)
            if current_string[0] != "":
                nodes.append(
                    textnode.Textnode(current_string[0], textnode.Texttype["Plain"])
                )
            nodes.append(
                textnode.Textnode(f"[{link[0]}]({link[1]})", textnode.Texttype["Link"])
            )
            current_string = current_string[1]
        if current_string != "":
            nodes.append(textnode.Textnode(current_string, textnode.Texttype["Plain"]))
    return nodes
