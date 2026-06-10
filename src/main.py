import os
import re
import shutil

import markdown_to_html


def main():
    BRANCH = os.getcwd()
    try:
        shutil.rmtree(f"{BRANCH}/public")
    except FileNotFoundError:
        pass
    os.mkdir(f"{BRANCH}/public")
    recursve_read_and_write(f"{BRANCH}/static", f"{BRANCH}/public", BRANCH)


def heading_extracter(html):
    head_text = re.findall(r"<h1>(.*?)</h1>", html)[0]
    html = re.sub(r"<h1># (.*?)</h1>", r"", html)
    head_text = re.sub(r"#", r"", head_text).strip()
    return head_text, html


def html_wrapper(markdown, template):
    html = markdown_to_html.markdown_to_html_node(markdown)
    # html = inline_list_elements(html)
    # print(html)
    head_text, html = heading_extracter(html)
    template = re.sub(r"{{ Title }}", head_text, template)
    template = re.sub(r"{{ Content }}", html, template)
    return template


def recursve_read_and_write(read_branch, write_branch, fetch_branch):
    for filename in os.listdir(read_branch):
        # print(f"{read_branch}/{filename}")
        if ".md" in filename:
            markdown = open(f"{read_branch}/{filename}", "r").read()
            html = html_wrapper(
                markdown, open(f"{fetch_branch}/template.html", "r").read()
            )
            # print(html)
            open(f"{write_branch}/{filename.replace('.md', '.html')}", "w").write(html)
            continue
        elif ".png" in filename or ".css" in filename:
            shutil.copy(f"{read_branch}/{filename}", f"{write_branch}/{filename}")
            continue
        elif os.path.isdir(f"{read_branch}/{filename}"):
            os.mkdir(f"{write_branch}/{filename}")
            recursve_read_and_write(
                f"{read_branch}/{filename}", f"{write_branch}/{filename}", fetch_branch
            )


main()
