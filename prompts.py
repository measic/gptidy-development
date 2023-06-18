from notebook_processing import *


def introduction_prompt(notebook, context):
    """What the project is about"""
    cell_contents = notebook.get_all_cells(include_outputs=False)
    return f"Write a concise 3-5 sentence introduction in markdown which gives an overview of this project's purpose, goals, and structure of topics. The context below provides background information and the cell contents is the notebook itself. Context: {context}. Cell contents: {cell_contents}"


def cell_process_prompt(notebook, cell_id, technical=True):
    """Describe what the code is doing"""
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']

    if technical:
        audience = "technical"
    else:
        audience = "non-technical"

    return f"Write a short 2-5 sentence description summarizing what this code is doing in markdown. Write it for a {audience} audience. Code: {str(cell_src)}"


def cell_result_prompt(notebook, cell_id, context, technical=True):
    """Explain the output of a cell"""
    # get relevant cell
    cell = notebook.get_single_cell(cell_id, include_outputs=True)
    cell = {'outputs': cell['outputs'], 'project_info': context}

    audience = "technical" if technical else "non-technical"

    return f"Write 2-4 sentences explaining the outputs of this code cell in markdown. Link the meaning of the outputs to the project. Write it for a {audience} audience. Cell contents: {str(cell)}"


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





def rename_variable(notebook, cell_id, variable, context):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
    {"role": "system", "content": "You are an expert at renaming variables in Python code to more meaningful names. You are very careful to rename all instances of a variable without changing anything else."},
        {"role" : "user", "content" : f"Rename the variable `{variable}` in the code delimited by triple backticks to a more meaningful name that reflects its usage and considers the project context. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the renamed variable) and `explanation` (a 1-2 sentence explanation of the new variable name)."},
        {"role" : "user", "content" : f"Project context:\n```{context}```"},
        {"role" : "user", "content" : f"Code:\n```{cell_src}```"},
        {"role" : "assistant", "content" : "updated_code:\n```"}
    ]
    return messages

def rename_function(notebook, cell_id, function_name, context):
    cell_src = notebook.get_single_cell(cell_id, include_outputs=False)['src']
    messages = [
    {"role": "system", "content": "You are an expert at renaming functions in Python code to more meaningful names. You are very careful to rename all instances of a function without changing anything else."},
        {"role" : "user", "content" : f"Rename the function `{function_name}` in the code delimited by triple backticks to a more meaningful name that reflects its usage and considers the project context. Do not add, remove, or change anything else. Structure your response under the following headings: `updated_code` (the code with the renamed function) and `explanation` (a 1-2 sentence explanation of the new function name)."},
        {"role" : "user", "content" : f"Project context:\n```{context}```"},
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