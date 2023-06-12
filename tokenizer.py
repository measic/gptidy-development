import tiktoken
import requests

TOKEN_LIMIT = 4096

# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens

# convert cells to list
def get_cell_list(notebook):
    # get all cells but only keep cell_type and source
    cells = []
    for i in range(len(notebook['cells'])):
        cell =  notebook['cells'][i]
        # if source is a list of strings, join them
        cell['source'] = ''.join(cell['source'])

        if cell['cell_type'] == 'code' and cell['outputs']:
            # i think the length is always 1?
            assert len(cell['outputs']) == 1
            # if output is a list of strings, join them
            cell['outputs'][0]['data']['text/plain'] = ''.join(cell['outputs'][0]['data']['text/plain'])

        cells.append({
            'id': i,
            'type': cell['cell_type'],
            'src': cell['source'],
            'outputs': cell['outputs'][0]['data']['text/plain'] if cell['cell_type'] == 'code' and cell['outputs'] else None
        })
    return cells

# take cells within subset of token limit
# not exact but a good approximation
def get_subset_cells(cells, token_limit):
    # filter out id and outputs in cells
    cells = [{'type': cell['type'], 'src': cell['src']} for cell in cells]

    # get content within token limit
    if num_tokens_from_string(str(cells)) <= token_limit:
        return cells
    else:
        tokens_per_cell = token_limit // len(cells)
        subset_cells = []
        for cell in cells:
            # take the limit_per_cell first tokens by adding each character until the limit is reached
            src = ''
            for char in cell['src']:
                if num_tokens_from_string(src) < tokens_per_cell:
                    src += char
                else:
                    break
            # append the cell to the subset
            subset_cells.append({
                'type': cell['type'],
                'src': src
            })
        return subset_cells

def get_notebook_contents_summary(notebook, token_limit=TOKEN_LIMIT // 2):
    cells = get_cell_list(notebook)
    subset_cells = get_subset_cells(cells, token_limit)
    return str(subset_cells)

def fetch_readme_helper(url):
    response = requests.get(url)
    if response.status_code == 200:
        project_info = response.text
        return project_info
    else:
        return None

def fetch_readme(url):
    # first try to get readme from this commit
    split_url = url.split('/')
    split_url = split_url[:6] + ['README.md']
    readme_url = '/'.join(split_url)
    readme = fetch_readme_helper(readme_url)
    if not readme:
        split_url[5] = 'master'
        readme_url = '/'.join(split_url)
        readme = fetch_readme_helper(readme_url)
        if not readme:
            split_url[5] = 'main'
            readme_url = '/'.join(split_url)
            readme = fetch_readme_helper(readme_url)
    return readme
    
def fetch_user_info(url):
    username = url.split('/', 4)[3]
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        return None
    
def fetch_notebook(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        notebook = response.json()
        return notebook
    else:
        return None

def get_project_info(url):
    user_info_full = fetch_user_info(url)
    readme_full = fetch_readme(url)
    project_info = {}

    if user_info_full is not None and (user_info_full['company'] or user_info_full['bio']):
        user_info = {}
        if user_info_full['company']:
            user_info['company'] = user_info_full['company']
        if user_info_full['bio']:
            user_info['bio'] = user_info_full['bio']
        project_info['user_info'] = user_info
    if readme_full is not None:
        project_info['readme'] = readme_full

    # if project_info contains any info, return it
    return project_info or None

def introduction_prompt(url):
    notebook = fetch_notebook(url)

    project_info = get_project_info(url)
    project_info_tokens = num_tokens_from_string(str(project_info))
    cell_contents = get_notebook_contents_summary(notebook, TOKEN_LIMIT - project_info_tokens)
    prompt = f"Write a concise 3-5 sentence introduction in markdown which gives an overview of this project's purpose, goals, and structure of topics. The context below provides background information and the cell contents is the notebook itself. Context: {project_info}. Cell contents: {cell_contents}"
    return prompt

def cell_process_prompt(url, cell_id):
    notebook = fetch_notebook(url)
    cells = get_cell_list(notebook)
    prompt = "Write a short 3-5 sentence description of what this code is doing in markdown. Cell contents: " + str({cells[cell_id]['src']})
    return prompt

def cell_reason_prompt(url, cell_id):
    notebook = fetch_notebook(url)
    cells = get_cell_list(notebook)
    prompt = "Write a short 3-5 sentence description explaining the output of this cell. Cell contents: " + str(cells[cell_id])
    return prompt
    
url = "https://raw.githubusercontent.com/ZaraYar/Analyzing-NYC-High-School-Data/f7de631936b9614ceb38f398327bc6695788970f~1/Basics.ipynb"

print(cell_reason_prompt(url, 0))