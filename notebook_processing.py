import github_api
import json


class Notebook:
    def __init__(self, notebook):
        self.notebook = notebook
        self.num_cells = len(notebook['cells'])

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
            src_lines = ''.join(src_lines)
        return src_lines

    def get_single_cell(self, cell_id, include_outputs=True):
        cell = self.notebook['cells'][cell_id]
        cell['source'] = ''.join(cell['source'])
        object = {
            'type': cell['cell_type'],
            'src': cell['source']
        }
        if include_outputs:
            object['outputs'] = self._get_single_cell_text_outputs(cell)
        return object

    def get_multiple_cells(self, cell_ids, include_outputs=True):
        return [self.get_single_cell(cell_id, include_outputs) for cell_id in cell_ids]

    def get_all_cells(self, include_outputs=True):
        return [self.get_single_cell(cell_id, include_outputs) for cell_id in range(self.num_cells)]

    def update_cell_src(self, cell_id, new_src):
        self.notebook['cells'][cell_id]['source'] = new_src
        print("Cell updated")

    def export_notebook_file(self):
        with open("file.ipynb", 'w') as f:
            json.dump(self.notebook, f)


def fetch_github_project_info(url):
    user_info_full = github_api.fetch_user_info(url)
    readme_full = github_api.fetch_readme(url)
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
