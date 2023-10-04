from notebook_processing import Notebook


introduction_main = """"Write an introductory cell in markdown for this Jupyter Notebook under the following headings:
- Title
- Background (2-4 sentences briefly introducing the wider topic)
- Goals (2-4 sentences specifically relating the wider topic to the purpose of the project)
- Structure (concise bulleted list of the organization of the notebook's cells)

Provided is 'Purpose' which provides background information to the project's purpose and 'Notebook' which includes all of the notebook's cells. Use these in your response."""

def introduction_prompt(notebook: Notebook):
    cell_contents = notebook.get_all_cells(include_outputs=False)
    messages = [
        {"role": "user", "content": introduction_main},
        {"role": "user", "content": f"Purpose:\n{notebook.purpose}"},
        {"role": "user", "content": f"Notebook:\n{cell_contents}"},
        {"role": "assistant", "content": "# Title"},
    ]
    return messages

summarize_cell = f"""Summarize this code cell under the following headings in markdown:
- Explanation (2-4 sentences summarizing what the code is doing)
- Reasoning (2-4 sentences linking the code to the project's purpose under a specific section in the introduction)
Provided below is the code cell itself as well as the introduction to the Jupyter Notebook"""

summarize_cell_plus_output = f"""Summarize this code cell under the following headings in markdown:
- Explanation (2-4 sentences summarizing what the code is doing)
- Reasoning (2-4 sentences linking the code to the project's purpose under a specific section in the introduction)
- Output (2-4 sentences interpreting the meaning of the output and linking this to the project)
Provided below is the code cell itself, its output, as well as the introduction to the Jupyter Notebook. Use these in your response."""

def summarize_cell_prompt(notebook: Notebook, introduction: str, cell_id: int):
    cell = notebook.get_single_cell(cell_id, include_outputs=True)
    cell_src = cell['src']
    cell_output = cell['outputs']

    messages = [
        {"role": "user", "content": summarize_cell_plus_output if cell_output else summarize_cell},
        {"role": "user", "content": f"Introduction:\n{introduction}"},
        {"role": "user", "content": f"Code cell:\n```python\n{cell_src}\n```"}
    ]
    if cell_output:
        messages.append({"role": "user", "content": f"Output:\n```{cell_output}```"})
    messages.append({"role": "assistant", "content": "## Explanation"})
    return messages

conclusion_main = """Write a conclusion in markdown for this Jupyter Notebook in past tense under the following headings:
- Summary (2-4 sentences very briefly reiterating the purpose and goals of the notebook and explaining what was done in the notebook)
- Interpretation (2-4 sentences interpreting key results, findings, or outputs and linking these to the project)

Provided is 'Introduction' which contains the introduction of the notebook and 'Notebook' which contains all cells and any associated outputs. Use these in your response."""

def conclusion_prompt(notebook: Notebook, introduction: str):
    cells = notebook.get_all_cells(include_outputs=False, include_markdown=True)

    messages = [
        {"role": "user", "content": conclusion_main},
        {"role": "user", "content": f"Introduction:\n{introduction}"},
        {"role": "user", "content": f"Notebook:\n{cells}"},
        {"role": "assistant", "content": "## Summary"}
    ]
    return messages