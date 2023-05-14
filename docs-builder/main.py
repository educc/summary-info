import markdown2
from pathlib import Path
from shutil import rmtree

PARENT_FOLDER = Path(__file__).parent.parent
FOLDER_SUBJECTS = PARENT_FOLDER / "subjects"
FOLDER_DOCS = PARENT_FOLDER / "docs"
TEMPLATE_FILE = Path(__file__).parent / "template.html"


def get_markdown_files() -> list[Path]:
    return list(FOLDER_SUBJECTS.glob("*.md"))

def markdown_to_html(markdown_file: Path) -> str:
    mdcontent = markdown_file.read_text()
    return markdown2.markdown(mdcontent)

def get_doc_folder() -> Path:
    """ It creates an empty doc folder, it deletes the previous one if it exists."""
    if FOLDER_DOCS.exists():
        rmtree(FOLDER_DOCS)

    if  not FOLDER_DOCS.exists():
        FOLDER_DOCS.mkdir()

    return FOLDER_DOCS

def create_index_file(folder: Path):
    """ It creates an index file with the list of all the files in the folder."""

    content = ""
    for file in folder.glob("*.html"):
        content += f"<li><a href='{file.name}'>{file.stem}</a></li>\n"
      
    html = TEMPLATE_FILE.read_text().format(content=content)

    (folder / "index.html").write_text(html)

def main():
    doc_path = get_doc_folder()

    for markdown_file in get_markdown_files():
        html = markdown_to_html(markdown_file)
        html_file = doc_path / (markdown_file.stem + ".html")
        html_file.write_text(html)

    create_index_file(doc_path)

if __name__ == "__main__":
    main()