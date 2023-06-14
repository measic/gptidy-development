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
