import json
import tiktoken

TOKEN_LIMIT = 4096

# read in jupyter notebook from file
with open("dynamicProgramming.ipynb", "r") as file:
    # Read the contents
    notebook = json.load(file)

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
        # if code cell is a list of strings, join them
        notebook['cells'][i]['source'] = ''.join(notebook['cells'][i]['source'])
        cells.append({
            'type': notebook['cells'][i]['cell_type'],
            'src': notebook['cells'][i]['source']
        })
    return cells

# take cells within subset of token limit
# not exact but a good approximation
def get_subset_cells(cells, token_limit):
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

def get_notebook_contents_summary(notebook, token_limit=500):
    cells = get_cell_list(notebook)
    subset_cells = get_subset_cells(cells, token_limit)
    return str(subset_cells)

test = get_notebook_contents_summary(notebook)
print(test)
print(num_tokens_from_string(test))