import os
import re
import shutil
import sys

import markdown_to_html


def main():
    URL = sys.argv[1]
    BRANCH = os.getcwd()
    try:
        shutil.rmtree(f"{BRANCH}/doc")
    except FileNotFoundError:
        pass
    os.mkdir(f"{BRANCH}/doc")
    recursve_read_and_write(f"{BRANCH}/static", f"{BRANCH}/doc", BRANCH, URL)


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


def recursve_read_and_write(read_branch, write_branch, fetch_branch, url):
    for filename in os.listdir(read_branch):
        if ".md" in filename:
            markdown = open(f"{read_branch}/{filename}", "r").read()
            html = html_wrapper(
                markdown, open(f"{fetch_branch}/template.html", "r").read()
            )
            html = re.sub(r'href="/', rf'href="{url}/', html)
            html = re.sub(r'src="/', rf'src="{url}/', html)
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


main()
