import github_api
from notebook_processing import *
from prompts import *

# setup notebook
url = "https://raw.githubusercontent.com/YerevaNN/mimic3-benchmarks/b37f83d2f432c67190c631ff554a1a832d9caaa5~1/mimic3benchmark/readers.py"

# # set project context
# right now fetching it from github readme + user company/bio but can write it myself too
project_context = "the project's purpose is to construct benchmark machine learning datasets from the MIMIC-III clinical database. I specifically focus on four key inpatient clinical prediction tasks: mortality prediction, decompensation detection, length of stay forecasting, and phenotype classification. My goal is to provide benchmarks for machine learning researchers in the healthcare field, aiming to accelerate progress, foster debate, and enable reproducibility and comparison of different ideas."

# print(project_context)

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


# context = "The purpose of this project is to provide a Python suite that constructs benchmark datasets for machine learning using the MIMIC-III clinical database. The project focuses on creating a multitask learning benchmark dataset for four key inpatient clinical prediction tasks, including mortality prediction, decompensation detection, length of stay forecasting, and phenotype classification."

# extract_variable = extract_variable(notebook, context=context, cell_id=2, segment='self._data[index][0]')

# introduction = "Analyzing Jeopardy Questions to Win Big\r\n\r\n# Background\r\n\r\nJeopardy is a popular TV game show where contestants answer questions to win money. In this project, we will analyze a dataset of Jeopardy questions to identify patterns in the questions that could help us win big.\r\n\r\n# Goals\r\n\r\nThe goal of this project is to answer the following questions:\r\n- How often do the answers appear in the questions?\r\n- How often are new questions repeats of older ones?\r\n- Are high-value questions harder or easier than low-value questions?\r\n- Which words commonly appear in high-value questions?\r\n\r\n# Structure\r\n\r\nThis notebook is organized into the following sections:\r\n- Data loading and cleaning\r\n- Answer overlap analysis\r\n- Question overlap analysis\r\n- High-value vs. low-value questions analysis\r\n- Common word analysis"


url = "https://raw.githubusercontent.com/gardiac2002/monkies/0f9e5514282d6b844c342f574c779bdc0b83ea4a~1/Sessions%20Analysis.ipynb"
# fetch notebook url
notebook = github_api.fetch_notebook(url)
# write contents to clone.ipynb
with open("clone.ipynb", "w") as f:
    json.dump(notebook, f)

notebook = Notebook(notebook)

print(notebook.get_all_cells(include_outputs=False, include_markdown=False))

