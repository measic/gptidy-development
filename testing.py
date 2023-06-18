import github_api
from notebook_processing import *
from prompts import *

# setup notebook
url = "https://raw.githubusercontent.com/ZaraYar/Analyzing-NYC-High-School-Data/f7de631936b9614ceb38f398327bc6695788970f/Basics.ipynb"
# read notebook in from file
with open("file.ipynb") as f:
    notebook = json.load(f)
notebook = Notebook(notebook)

# set project context
# right now fetching it from github readme + user company/bio but can write it myself too
project_context = fetch_github_project_info(url)

# generating different prompts
introduction_md = introduction_prompt(notebook, project_context)

process_md = cell_process_prompt(notebook, cell_id=3, technical=False)

result_md = cell_result_prompt(
    notebook, context=project_context, cell_id=0, technical=False)

summary_md = cell_summary_prompt(
    notebook, cell_ids=[0, 1, 2, 3], technical=False)

rename_variable_md = rename_variable(
    notebook, cell_id=10, variable="i", context=project_context)

remove_unused_variables = remove_unused_variables(notebook, cell_id=12)

remove_unused_functions = remove_unused_functions(notebook, cell_id=8)

format_code = format_code(notebook, cell_id=12)

rename_variable = rename_variable(notebook, context="analyzing jeopardy data", cell_id=10, variable="val")

rename_function = rename_function(notebook, context="analyzing jeopardy data", cell_id=10, function_name="function")

