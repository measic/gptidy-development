def format_code_prompt(notebook, cell_id):
    cell = notebook.get_single_cell(cell_id, include_outputs=False)
    cell_src = cell['src']

    task = r"Format the code delimited by triple backticks according to PEP 8 conventions. Do not add, remove, or change anything else. Structure your response under the following headings: 'Identified formatting issues' (a short paragraph describing the formatting issues) and 'Formatted code' (e.g., ```python\n#full code with all formatting issues fixed\n```)."

    messages = [
        {"role": "user", "content": task},
        {"role": "user", "content": f"```python\n{cell_src}\n```"},
    ]
    return messages
