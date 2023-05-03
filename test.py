# read in a json file
import json
with open('notebooks/test.ipynb') as f:
    data = json.load(f)

cell1 = data['cells'][2].get('source')

context = "im a data scientist. this project is about heart attack analysis and prediction. the main point is to predict if a person is vulnerable to a heart attack or not"
print(cell1)