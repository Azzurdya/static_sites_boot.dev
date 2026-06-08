import os
import re
import shutil

import markdown_to_html


def main():
    branch = os.getcwd()
    shutil.rmtree(f"{branch}/public")
    os.mkdir(f"{branch}/public")
    markdown = open(f"{branch}/src/source.md", "r").read()
    template = open(f"{branch}/template.html", "r").read()
    html = html_wrapper(markdown, template)
    open(f"{branch}/static/source.html", "w").write(html)
    shutil.copytree(f"{branch}/static", f"{branch}/public", dirs_exist_ok=True)
    new_public_files = os.listdir(f"{branch}/public")
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
