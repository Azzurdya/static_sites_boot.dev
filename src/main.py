import os
import shutil

import markdown_to_html


def main():
    public_files = os.listdir("../public")
    source_files = os.listdir("../static")
    print(public_files)
    for file in public_files:
        if os.path.exists(f"../public/{file}"):
            os.remove(f"../public/{file}")
    for file in source_files:
        if os.path.exists(f"../static/{file}"):
            shutil.copy(f"../static/{file}", f"../public/{file}")
        if file == "source.html":
            markdown = open(f"../src/source.md", "r").read()
            html = f"<html><body>{markdown_to_html.markdown_to_html_node(markdown)}</body></html>"
            print(html)
            open(f"../public/{file}", "w").write(html)
    new_public_files = os.listdir("../public")
    return new_public_files


print(main())
