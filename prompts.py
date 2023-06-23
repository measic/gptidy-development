from notebook_processing import *

def introduction_prompt(notebook, context):
    """What the project is about"""
    cell_contents = notebook.get_all_cells(include_outputs=False)
    messages = [
        {"role": "system", "content": "You are an expert at writing introductions for Python projects."},
        {"role": "user", "content": "Write an introductory cell in markdown for this Jupyter Notebook under the following headings:\n- Title\n- Background (2-3 sentences briefly introducing the wider topic)\n- Goals (2-3 sentences specifically relating the wider topic to the purpose of the project)\n- Structure (concise bulleted list of the organization of the notebook's cells)\n`Context` provides background information to the project and `Notebook` contains all cells."},
        {"role": "user", "content": f"Context:\n```{context}```"},
        {"role": "user", "content": f"Notebook:\n```{cell_contents}```"},
        {"role": "assistant", "content": "# Title"},
    ]
    return messages

def cell_summarize_prompt(notebook: Notebook, introduction: str, cell_id: int):
    cell = notebook.get_single_cell(cell_id, include_outputs=True)
    cell_src = cell['src']
    cell_output = cell['outputs']
    includes_output = True if cell_output else False

    output_msg = '- Output (2-3 sentences interpreting the meaning of the output and linking its meaning to the project)\n' if includes_output else ''
    messages = [
        {"role": "system", "content": "You are an expert at summarizing code cells in Jupyter Notebooks."},
        {"role": "user", "content": f"Summarize this code cell under the following headings in markdown:\n- Explanation (2-3 sentences summarizing what the code is doing)\n- Reasoning (2-3 sentences linking the code to the purpose of the project under a specific section)\n{output_msg}Provided below is the code cell itself{', its output,' if includes_output else ''} as well as the introduction to the Jupyter Notebook"},
        {"role": "user", "content": f"Introduction:\n```{introduction}```"},
        {"role": "user", "content": f"Code cell:\n```{cell_src}```"}
    ]
    if includes_output:
        messages.append({"role": "user", "content": f"Output:\n```{cell_output}```"})
    messages.append({"role": "assistant", "content": "# # Explanation"})
    return messages

def cell_summary_prompt(notebook, cell_ids, technical=True):
    """Summarize what has been done for a collection of code cells"""
    # get relevant cells
    cells = notebook.get_multiple_cells(cell_ids, include_outputs=False)

    # verify that the cells we are looking for are code cells
    for cell in cells:
        if cell['type'] != 'code':
            raise ValueError("Cell is not a code cell")

    # keep only src
    cells = [{'src': cell['src']} for cell in cells]

    audience = "technical" if technical else "non-technical"

    return f"Write a 3-5 sentence conclusion for this project. Write it for a {audience} audience. Cell contents: {cells}"

def extract_variable(notebook: Notebook, cell_id: int, segment: str, context: str):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
    {"role": "system", "content": "You are an expert at extracting variables in Python code and giving extracted variables meaningful names."},
        {"role" : "user", "content" : f"Extract and replace the segment delimited by double backticks as a variable in the code delimited by triple backticks. Give the extracted variable a meaningful name based on its usage and project context. Do not add, remove, or change anything else. Structure your response under the following headings: `Updated code` (the code with the extracted variable) and `Explanation` (a 1-2 sentence explanation of the extracted variable's name)."},
        {"role" : "user", "content" : f"Project context:\n`{context}`"},
        {"role" : "user", "content" : f"Segment to extract:\n``{segment}``"},
        {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
        {"role" : "assistant", "content" : "Updated code:\n```"}
    ]
    return messages

def extract_function(notebook, cell_id, lines, context):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    segment = notebook.get_single_cell_src_lines(cell_id, lines)
    messages = [
    {"role": "system", "content": "You are an expert at extracting functions in Python code and giving extracted functions meaningful names."},
        {"role" : "user", "content" : f"Extract and replace the segment delimited by double backticks as a function in the code delimited by triple backticks. Give the function a meaningful name based on its usage and project context.  Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the extracted function) and `explanation` (a 1-2 sentence explanation of the function name)."},
        {"role" : "user", "content" : f"Project context:\n`{context}`"},
        {"role" : "user", "content" : f"Segment to extract:\n``{segment}``"},
        {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
        {"role" : "assistant", "content" : "updated_code:\n```"}
    ]
    return messages

def rename_variable(notebook, cell_id, variable, context):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
    {"role": "system", "content": "You are an expert at renaming variables in Python code to more meaningful names. You are very careful to rename all instances of a variable without changing anything else."},
        {"role" : "user", "content" : f"Rename the variable `{variable}` in the code delimited by triple backticks to a more meaningful name that reflects its usage and considers the project context. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the renamed variable) and `explanation` (a 1-2 sentence explanation of the new variable name)."},
        {"role" : "user", "content" : f"Project context:\n`{context}`"},
        {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
        {"role" : "assistant", "content" : "updated_code:\n```"}
    ]
    return messages

def rename_function(notebook, cell_id, function_name, context):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
    {"role": "system", "content": "You are an expert at renaming functions in Python code to more meaningful names. You are very careful to rename all instances of a function without changing anything else."},
        {"role" : "user", "content" : f"Rename the function `{function_name}` in the code delimited by triple backticks to a more meaningful name that reflects its usage and considers the project context. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the renamed function) and `explanation` (a 1-2 sentence explanation of the new function name)."},
        {"role" : "user", "content" : f"Project context:\n`{context}`"},
        {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
        {"role" : "assistant", "content" : "updated_code:\n```"}
    ]
    return messages

def remove_unused_variables(notebook, cell_id):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
        {"role": "system", "content": "You are an expert at identifying and removing unused variable definitions in Python code. You are very careful to remove all unused variables without removing any used variables."},
        {"role": "user", "content": "Remove unused variable definitions in the code delimited by triple backticks. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the unused variables removed) and `unused_variables` (a list of variable names)."},
        {"role": "user", "content": f"```{cell_src}```"},
        {"role": "assistant", "content": "updated_code:\n```"},
    ]
    return messages

def remove_unused_functions(notebook, cell_id):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
        {"role": "system", "content": "You are an expert at identifying and removing unused function definitions in Python code. You are very careful to remove all unused functions without removing any used functions."},
        {"role": "user", "content": "Remove unused function definitions in the code delimited by triple backticks. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the unused functions removed) and `unused_functions` (a list of function names)."},
        {"role": "user", "content": f"```{cell_src}```"},
        {"role": "assistant", "content": "updated_code:\n```"},
    ]
    return messages

def format_code(notebook, cell_id):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
        {"role": "system", "content": "You are an expert in formatting Python code according to PEP 8 conventions."},
        {"role": "user", "content": "Format the code delimited by triple backticks according to PEP 8 conventions. Do not add, remove, or change anything else. Structure your response under the following headings: `formatted_code` (the formatted code) and `changes` (a list of formatting changes)."},
        {"role": "user", "content": f"```{cell_src}```"},
        {"role": "assistant", "content": "formatted_code:\n```"},
    ]
    return messages