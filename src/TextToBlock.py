import re

BLOCKTYPES = {
    "p": "paragraph",
    "h": "heading",
    "c": "code",
    "q": "quote",
    "u": "unordered_list",
    "o": "ordered_list",
}


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] == "":
            blocks.pop(i)
    return blocks


def is_valid_ordered_list(block):
    lines = block.split("\n")
    for i, line in enumerate(lines, start=1):
        pattern = rf"^{i}\.\s+.*$"
        if not re.match(pattern, line):
            return False
    return True


def block_to_type(block):
    if re.match(r"#{1,6}\s+(?!.*#)(.+)", block):  # Updated regex for headings
        return BLOCKTYPES["h"]
    elif re.match(r"```\n(.*)\n```", block, re.DOTALL):
        return BLOCKTYPES["c"]
    elif re.match(r"^>\s+.*$", block, re.MULTILINE):
        return BLOCKTYPES["q"]
    elif re.match(r"^- .*$", block, re.MULTILINE):
        return BLOCKTYPES["u"]
    elif is_valid_ordered_list(block):
        return BLOCKTYPES["o"]
    else:
        return BLOCKTYPES["p"]
