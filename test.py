# read in a json file
import json
from api import *
with open('notebooks/interactive-analysis-of-football-data.ipynb') as f:
    data = json.load(f)

cell1 = data['cells'][20].get('source')

context = "im a data scientist. this project is about heart attack analysis and prediction. the main point is to predict if a person is vulnerable to a heart attack or not"
content = ''.join(cell1)
operation = prompts[Operation.RenameVariable]["prompt"]("'data'")

# create json object consisting of context, content, and operation

response = get_response(context, content, operation)

print(response)