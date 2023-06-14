import github_api
from notebook_processing import *
from prompts import *

# setup notebook
url = "https://raw.githubusercontent.com/ZaraYar/Analyzing-NYC-High-School-Data/f7de631936b9614ceb38f398327bc6695788970f/Basics.ipynb"
notebook = github_api.fetch_notebook(url)
notebook = Notebook(notebook)

# set project context
# right now fetching it from github readme + user company/bio but can write it myself too
project_context = fetch_github_project_info(url)

# generating different prompts
introduction_md = introduction_prompt(notebook, project_context)

process_md = cell_process_prompt(notebook, cell_id=3, technical=False)

result_md = cell_result_prompt(
    notebook, context=project_context, cell_id=5, technical=False)

summary_md = cell_summary_prompt(
    notebook, cell_ids=[0, 1, 2, 3], technical=False)
