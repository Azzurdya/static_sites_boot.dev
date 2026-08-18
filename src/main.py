import os
import re
import shutil
import sys

import markdown_to_html


def main():
    try:
        URL = sys.argv[1]
    except IndexError:
        URL = ""
    BRANCH = os.getcwd()
    try:
        shutil.rmtree(f"{BRANCH}/docs")
    except FileNotFoundError:
        pass
    os.mkdir(f"{BRANCH}/docs")
    recursve_read_and_write(f"{BRANCH}/static", f"{BRANCH}/docs", BRANCH, URL)


def heading_extracter(html):
    head_text = re.findall(r"<h1>(.*?)</h1>", html)[0]
    html = re.sub(r"<h1># (.*?)</h1>", r"", html)
    head_text = re.sub(r"#", r"", head_text).strip()
    return head_text, html


def html_wrapper(markdown, template, url):
    html = markdown_to_html.markdown_to_html_node(markdown)
    head_text, html = heading_extracter(html)
    template = re.sub(r"{{ Title }}", head_text, template)
    template = re.sub(r"{{ Content }}", html, template)
    if url != "":
        template = replace_link(template, url)

    return template


def recursve_read_and_write(read_branch, write_branch, fetch_branch, url):
    for filename in os.listdir(read_branch):
        if ".md" in filename:
            markdown = open(f"{read_branch}/{filename}", "r").read()
            html = html_wrapper(
                markdown, open(f"{fetch_branch}/template.html", "r").read(), url
            )
            open(f"{write_branch}/{filename.replace('.md', '.html')}", "w").write(html)
            continue
        elif ".png" in filename or ".css" in filename:
            shutil.copy(f"{read_branch}/{filename}", f"{write_branch}/{filename}")
            continue
        elif os.path.isdir(f"{read_branch}/{filename}"):
            os.mkdir(f"{write_branch}/{filename}")
            recursve_read_and_write(
                f"{read_branch}/{filename}",
                f"{write_branch}/{filename}",
                fetch_branch,
                url,
            )


def replace_link(html, url):
    links = re.findall(r"<a href='(.*?)'>", html)
    src = re.findall(r"<img src='(.*?)'>", html)
    head = re.findall(r'<link href="(.*?)"', html)
    for link in links:
        if link == "/":
            html = re.sub(rf"<a href='{link}'", rf"<a href='{url}'", html)
        elif link.startswith("https://"):
            pass
        else:
            html = re.sub(rf"<a href='{link}'", rf"<a href='{url}{link}'", html)
    for s in src:
        html = re.sub(rf"<img src='{s}'", rf"<img src='{url}{s}'", html)
    for h in head:
        html = re.sub(rf'<link href="{h}"', rf'<link href="{url}{h}"', html)

    return html


main()
