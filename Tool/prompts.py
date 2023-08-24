from notebook_processing import *

def introduction_prompt(notebook, context):
    cell_contents = notebook.get_all_cells(include_outputs=False)
    messages = [
        {"role": "system", "content": "You are an expert at writing introductions for Jupyter Notebooks."},
        {"role": "user", "content": "Write an introductory cell in markdown for this Jupyter Notebook under the following headings:\n- Title\n- Background (2-3 sentences briefly introducing the wider topic)\n- Goals (2-3 sentences specifically relating the wider topic to the purpose of the project)\n- Structure (concise bulleted list of the organization of the notebook's cells)\n`Context` provides background information to the project and `Notebook` contains all cells."},
        {"role": "user", "content": f"Context:\n```{context}```"},
        {"role": "user", "content": f"Notebook:\n```{cell_contents}```"},
        {"role": "assistant", "content": "# Title"},
    ]
    return messages

def summarize_cell_prompt(notebook: Notebook, introduction: str, cell_id: int):
    cell = notebook.get_single_cell(cell_id, include_outputs=True)
    cell_src = cell['src']
    cell_output = cell['outputs']
    includes_output = True if cell_output else False

    output_msg = '- Output (2-3 sentences interpreting the meaning of the output and linking this to the project)\n' if includes_output else ''
    messages = [
        {"role": "system", "content": "You are an expert at summarizing code cells in Jupyter Notebooks."},
        {"role": "user", "content": f"Summarize this code cell under the following headings in markdown:\n- Explanation (2-3 sentences summarizing what the code is doing)\n- Reasoning (2-3 sentences linking the code to the project's purpose under a specific section)\n{output_msg}Provided below is the code cell itself{', its output,' if includes_output else ''} as well as the introduction to the Jupyter Notebook"},
        {"role": "user", "content": f"Introduction:\n```{introduction}```"},
        {"role": "user", "content": f"Code cell:\n```{cell_src}```"}
    ]
    if includes_output:
        messages.append({"role": "user", "content": f"Output:\n```{cell_output}```"})
    messages.append({"role": "assistant", "content": "## Explanation"})
    return messages

def conclusion_prompt(notebook: Notebook, introduction: str):
    cells = notebook.get_all_cells(include_outputs=True)

    messages = [
        {"role": "system", "content": "You are an expert at writing conclusions for Jupyter Notebooks."},
        {"role": "user", "content": "Write a conclusion in markdown for this Jupyter Notebook in past tense under the following headings:\n- Summary (2-3 sentences very briefly reiterating the purpose and goals of the notebook and explaining what was done in the notebook)\n- Interpretation (2-3 sentences interpreting key results, findings, or outputs and linking these to the project)\nProvided below is `Introduction` which contains the introduction of the notebook and `Notebook` which contains all cells and any associated outputs."},
        {"role": "user", "content": f"Introduction:\n```{introduction}```"},
        {"role": "user", "content": f"Notebook:\n```{cells}```"},
        {"role": "assistant", "content": "## Summary"}
    ]
    return messages

# def extract_variable(notebook: Notebook, cell_id: int, segment: str, context: str):
#     cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
#     messages = [
#     {"role": "system", "content": "You are an expert at extracting variables in Python code and giving extracted variables meaningful names."},
#         {"role" : "user", "content" : f"Extract and replace the segment delimited by double backticks as a variable in the code delimited by triple backticks. Give the extracted variable a meaningful name based on its usage and project context. Do not add, remove, or change anything else. Structure your response under the following headings: `Updated code` (the code with the extracted variable) and `Explanation` (a 1-2 sentence explanation of the extracted variable's name)."},
#         {"role" : "user", "content" : f"Project context:\n`{context}`"},
#         {"role" : "user", "content" : f"Segment to extract:\n``{segment}``"},
#         {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
#         {"role" : "assistant", "content" : "Updated code:\n```"}
#     ]
#     return messages

# def extract_function(notebook, cell_id, lines, context):
#     cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
#     segment = notebook.get_single_cell_src_lines(cell_id, lines)
#     messages = [
#     {"role": "system", "content": "You are an expert at extracting functions in Python code and giving extracted functions meaningful names."},
#         {"role" : "user", "content" : f"Extract and replace the segment delimited by double backticks as a function in the code delimited by triple backticks. Give the function a meaningful name based on its usage and project context.  Do not add, remove, or change anything else. Structure your response under the following headings: `Updated code` (the code with the extracted function) and `Explanation` (a 1-2 sentence explanation of the function name)."},
#         {"role" : "user", "content" : f"Project context:\n`{context}`"},
#         {"role" : "user", "content" : f"Segment to extract:\n``{segment}``"},
#         {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
#         {"role" : "assistant", "content" : "Updated code:\n```"}
#     ]
#     return messages