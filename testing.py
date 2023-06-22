import github_api
from notebook_processing import *
from prompts import *

# setup notebook
url = "https://raw.githubusercontent.com/YerevaNN/mimic3-benchmarks/b37f83d2f432c67190c631ff554a1a832d9caaa5~1/mimic3benchmark/readers.py"
# read notebook in from file
with open("sample.ipynb") as f:
    notebook = json.load(f)
notebook = Notebook(notebook)

# # set project context
# right now fetching it from github readme + user company/bio but can write it myself too
project_context = fetch_github_project_info(url)

# # generating different prompts
# introduction_md = introduction_prompt(notebook, project_context)

# process_md = cell_process_prompt(notebook, cell_id=3, technical=False)

# result_md = cell_result_prompt(
#     notebook, context=project_context, cell_id=0, technical=False)

# summary_md = cell_summary_prompt(
#     notebook, cell_ids=[0, 1, 2, 3], technical=False)

# rename_variable_md = rename_variable(
#     notebook, cell_id=10, variable="i", context=project_context)

# remove_unused_variables = remove_unused_variables(notebook, cell_id=12)

# remove_unused_functions = remove_unused_functions(notebook, cell_id=8)

# format_code = format_code(notebook, cell_id=12)

# rename_variable = rename_variable(notebook, context="analyzing jeopardy data", cell_id=10, variable="val")

# rename_function = rename_function(notebook, context="analyzing jeopardy data", cell_id=10, function_name="function")

# extract_function = extract_function(notebook, context="this project is about analyzing jeopardy data", cell_id=7, lines=(3,13))


context = "The purpose of this project is to provide a Python suite that constructs benchmark datasets for machine learning using the MIMIC-III clinical database. The project focuses on creating a multitask learning benchmark dataset for four key inpatient clinical prediction tasks, including mortality prediction, decompensation detection, length of stay forecasting, and phenotype classification."

extract_variable = extract_variable(notebook, context=context, cell_id=2, segment='self._data[index][0]')
