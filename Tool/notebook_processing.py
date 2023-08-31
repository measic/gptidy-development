import json
import tiktoken
from math import floor

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens

class Notebook:
    def __init__(self, notebook=None, file_path=None):
        if notebook is None and file_path is not None:
            self._read_notebook_file(file_path)
        elif notebook is not None and file_path is None:
            self.notebook = notebook
        else:
            raise Exception("Must provide either notebook or file_path, not both or none")
        self.num_cells = len(self.notebook['cells'])
        self._join_each_cell()
        self.purpose = None

    def _read_notebook_file(self, file_path):
        with open(file_path) as f:
            self.notebook = json.load(f)

    def _join_each_cell(self):
        for cell in self.notebook['cells']:
            cell['source'] = ''.join(cell['source'])

    def _get_single_cell_text_outputs(self, cell):
        # if the cell has outputs
        if cell['cell_type'] == 'code' and cell['outputs']:
            outputs = cell['outputs']
            relevant_outputs = []
            # look through each output
            for output in outputs:
                # if the output has 'data' (most cases)
                if "data" in output:
                    # we only consider text/plain keys
                    for key in output['data']:
                        if key == 'text/plain':
                            # convert outputs to string format
                            output_as_string = ''.join(output['data'][key])
                            relevant_outputs.append(output_as_string)
                # if the output has 'name' (only seen one case so far)
                elif "text" in output:
                    # convert outputs to string format
                    output_as_string = ''.join(output['text'])
                    relevant_outputs.append(output_as_string)
                # if the output has 'value' (only seen one case so far) 
                elif "evalue" in output:
                    # convert outputs to string format
                    output_as_string = ''.join(output['evalue'])
                    relevant_outputs.append(output_as_string)
                # this should not happen
                else:
                    raise Exception("No data or name in output")
        else:
            relevant_outputs = None
        return relevant_outputs
    
    def get_single_cell_src_lines(self, cell_id, lines):
        cell = self.notebook['cells'][cell_id]
        if type(cell['source']) == list:
            src_lines = cell['source'][lines[0]:lines[1] + 1]
        else:
            assert type(cell['source']) == str
            src_lines = cell['source'].split('\n')[lines[0]:lines[1] + 1]
        return ''.join(src_lines)

    def get_single_cell(self, cell_id, include_outputs=True, tokens=None):
        cell = self.notebook['cells'][cell_id]
        cell['source'] = ''.join(cell['source'])
        object = {
            'id': cell_id,
            'type': cell['cell_type'],
            'src': cell['source'] if tokens is None else cell['source'][:tokens],
        }
        if include_outputs:
            output = self._get_single_cell_text_outputs(cell)
            if output:
                object['outputs'] = output if tokens is None else output[:tokens]
        return object

    def get_multiple_cells(self, cell_ids, include_outputs=True):
        return [self.get_single_cell(cell_id, include_outputs) for cell_id in cell_ids]

    def get_all_cells(self, token_limit=None, include_outputs=True, include_markdown=True):
        if token_limit is None:
            return [self.get_single_cell(cell_id, include_outputs) for cell_id in range(self.num_cells) if include_markdown or self.notebook['cells'][cell_id]['cell_type'] != 'markdown']
        else:
            # divide by token limit to get how many tokens each cell should have
            tokens_per_cell = floor(token_limit / self.num_cells)
            print(tokens_per_cell)
            # now we take all cells but only take tokens_per_cell tokens from each cell
            return [self.get_single_cell(cell_id, include_outputs, tokens_per_cell) for cell_id in range(self.num_cells) if include_markdown or self.notebook['cells'][cell_id]['cell_type'] != 'markdown']
        
    def update_cell_src(self, cell_id, new_src):
        self.notebook['cells'][cell_id]['source'] = new_src
        print("Cell updated")

    def export_notebook_file(self):
        with open("file.ipynb", 'w') as f:
            json.dump(self.notebook, f)
    
    def get_average_cell_length(self):
        total_length = 0
        for cell in self.notebook['cells']:
            total_length += len(cell['source'])
        return total_length / self.num_cells
    
    def get_average_md_cell_length(self):
        total_length = 0
        num_md_cells = 0
        for cell in self.notebook['cells']:
            if cell['cell_type'] == 'markdown':
                num_md_cells += 1
                total_length += len(cell['source'])
        return total_length / num_md_cells

    def get_average_code_cell_length(self):
        total_length = 0
        num_code_cells = 0
        for cell in self.notebook['cells']:
            if cell['cell_type'] == 'code':
                num_code_cells += 1
                total_length += len(cell['source'])
        return total_length / num_code_cells

    def get_number_of_code_cells(self):
        return len([cell for cell in self.notebook['cells'] if cell['cell_type'] == 'code'])

    def get_number_of_md_cells(self):
        return len([cell for cell in self.notebook['cells'] if cell['cell_type'] == 'markdown'])