import re


def extract_markdown_images(text):
    markdown_image_def = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return markdown_image_def


def extract_markdown_links(text):
    markdown_link_def = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return markdown_link_def
