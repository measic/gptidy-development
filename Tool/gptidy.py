import sys
import json
from notebook_processing import Notebook 
from gpt.gpt import gpt_wrapper, gpt_unpack_simple
from gpt.prompts import introduction_prompt, summarize_cell_prompt, conclusion_prompt

class GPTidy:
    def __init__(self, notebook: Notebook):
        self.notebook = notebook
    
    def generate_introduction(self):
        introduction = introduction_prompt(self.notebook)
        introduction = gpt_wrapper(introduction)
        introduction = gpt_unpack_simple(introduction)
        return introduction

if __name__ == "__main__":
    # parse file
    if len(sys.argv) < 2:
        print("Usage: python3 gptidy.py <path to notebook>")
        sys.exit(1)
    file_path = sys.argv[1]

    # read in notebook using io
    with open(file_path, 'r') as f:
        notebook = json.load(f)

    notebook = Notebook(notebook)

    # ask for purpose
    purpose = input("What is the purpose of this notebook?")
    notebook.purpose = purpose

    gptidy = GPTidy(notebook)

    # generate introduction
    introduction = gptidy.generate_introduction()
    print(introduction)