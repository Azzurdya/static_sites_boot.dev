import os
import re
import shutil

import markdown_to_html


def main():
    source = os.getcwd()
    print(source)
    public_files = os.listdir(f"{source}/public")
    source_files = os.listdir(f"{source}/static")
    print(public_files)
    for file in public_files:
        if os.path.exists(f"{source}/public/{file}"):
            os.remove(f"{source}/public/{file}")
    for file in source_files:
        if os.path.exists(f"{source}/static/{file}"):
            shutil.copy(f"{source}/static/{file}", f"{source}/public/{file}")
        if file == "source.html":
            markdown = open(f"{source}/src/source.md", "r").read()
            template = open(f"{source}/template.html", "r").read()
            html = html_wrapper(markdown, template)
            print(html)
            open(f"{source}/public/{file}", "w").write(html)
    new_public_files = os.listdir(f"{source}/public")
    return new_public_files


def heading_extracter(html):
    head_text = re.findall(r"<h1>(.*?)</h1>", html)[0]
    html = re.sub(r"<h1># (.*?)</h1>", r"", html)
    head_text = re.sub(r"#", r"", head_text).strip()
    return head_text, html


def html_wrapper(markdown, template):
    html = markdown_to_html.markdown_to_html_node(markdown)
    head_text, html = heading_extracter(html)
    template = re.sub(r"{{ Title }}", head_text, template)
    template = re.sub(r"{{ Content }}", html, template)
    return template


print(main())
