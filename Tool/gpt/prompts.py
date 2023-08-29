

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