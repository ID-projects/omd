import re
import sys
from pathlib import Path

import nbformat

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def add_cells(notebook, text):
    pattern = re.compile(r"```\s*(?:python|py)\s*\n?(.*?)\n?```", re.DOTALL)
    matches = list(pattern.finditer(text))

    markdown_parts = []
    code_cells = []
    last_end = 0
    for match in matches:
        before = text[last_end:match.start()].strip()
        if before:
            markdown_parts.append(before)

        code = match.group(1).strip()
        if code:
            code_cells.append(nbformat.v4.new_code_cell(code))

        last_end = match.end()

    tail = text[last_end:].strip()
    if tail:
        markdown_parts.append(tail)

    markdown = "\n\n".join(markdown_parts)
    if markdown:
        notebook.cells.append(nbformat.v4.new_markdown_cell(markdown))

    notebook.cells.extend(code_cells)


def main():
    script_dir = Path(__file__).resolve().parent
    task_files = sorted(script_dir.glob("task_*.md"))

    if not task_files:
        print("Не найдены файлы task_*.md рядом со скриптом.")
        return

    notebook = nbformat.v4.new_notebook()

    for task_path in task_files:
        text = task_path.read_text(encoding="utf-8")
        add_cells(notebook, text)

    output_path = script_dir / "tasks.ipynb"
    nbformat.write(notebook, output_path)

    print(f"Создан ноутбук: {output_path}")


if __name__ == "__main__":
    main()