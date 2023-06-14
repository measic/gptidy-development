import tiktoken

# take cells within subset of token limit
# not exact but a good approximation


def get_subset_cells(cells, token_limit):
    # filter out outputs in cells
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


# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens
