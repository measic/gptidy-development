import json


class Notebook:
    def __init__(self, notebook):
        self.notebook = notebook
        self.num_cells = len(notebook['cells'])
        self.purpose = None

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

    def get_single_cell(self, cell_id, include_outputs=True):
        cell = self.notebook['cells'][cell_id]
        cell['source'] = ''.join(cell['source'])
        object = {
            'id': cell_id,
            'type': cell['cell_type'],
            'src': cell['source']
        }
        if include_outputs:
            output = self._get_single_cell_text_outputs(cell)
            if output:
                object['outputs'] = output
        return object

    def get_multiple_cells(self, cell_ids, include_outputs=True):
        return [self.get_single_cell(cell_id, include_outputs) for cell_id in cell_ids]

    def get_all_cells(self, include_outputs=True, include_markdown=True):
        return [self.get_single_cell(cell_id, include_outputs) for cell_id in range(self.num_cells) if include_markdown or self.notebook['cells'][cell_id]['cell_type'] != 'markdown']

    def update_cell_src(self, cell_id, new_src):
        self.notebook['cells'][cell_id]['source'] = new_src
        print("Cell updated")

    def export_notebook_file(self):
        with open("file.ipynb", 'w') as f:
            json.dump(self.notebook, f)